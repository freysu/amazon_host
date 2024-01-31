import os
import re
import json
import logging
import time
from retrying import retry
from datetime import datetime, timezone, timedelta
from typing import Optional, List
from aiohttp import ClientSession, ClientTimeout, ClientTimeout, TCPConnector
from pythonping import ping
import aiofiles
import socket
import asyncio

HOSTS_TEMPLATE = """# Amazon Host Start
{content}

# Update time: {update_time}
# Update url: https://raw.githubusercontent.com/freysu/amazon_host/main/hosts
# Star me: https://github.com/reysu/amazon_host
# Amazon Host End\n"""

SCRIPT_DIR = os.path.dirname(__file__)
README_PATH = os.path.join(SCRIPT_DIR, "README.md")
README_TEMPLATE_PATH = os.path.join(SCRIPT_DIR, "README_template.md")
HOSTS_PATH = os.path.join(SCRIPT_DIR, "hosts")
HOSTS_JSON_PATH = os.path.join(SCRIPT_DIR, "hosts.json")
AMAZON_URLS_FILE = os.path.join(SCRIPT_DIR, "amazon_urls.txt")
PING_TIMEOUT = 2
MAX_ATTEMPTS = 5
CONCURRENT_REQUESTS = 5

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

with open(AMAZON_URLS_FILE, "r") as file:
    AMAZON_URLS = [line.strip() for line in file if line.strip()]


async def write_file(hosts_content: str, update_time: str) -> bool:
    output_doc_file_path = README_PATH
    template_path = README_TEMPLATE_PATH
    await write_host_file(hosts_content)

    if os.path.exists(output_doc_file_path):
        async with aiofiles.open(output_doc_file_path, "r", encoding="utf-8") as old_readme_fb:
            old_content = await old_readme_fb.read()
            if old_content:
                old_hosts = old_content.split("```bash")[1].split("```")[0].strip()
                old_hosts = old_hosts.split("# Update time:")[0].strip()
                hosts_content_hosts = hosts_content.split("# Update time:")[0].strip()
                if old_hosts == hosts_content_hosts:
                    logger.info("Host not changed")
                    return False

    async with aiofiles.open(template_path, "r", encoding="utf-8") as temp_fb:
        template_str = await temp_fb.read()
        hosts_content = template_str.format(
            hosts_str=hosts_content, update_time=update_time
        )
        async with aiofiles.open(output_doc_file_path, "w", encoding="utf-8") as output_fb:
            await output_fb.write(hosts_content)
    return True


async def write_host_file(hosts_content: str) -> None:
    output_file_path = HOSTS_PATH
    async with aiofiles.open(output_file_path, "w", encoding="utf-8") as output_fb:
        await output_fb.write(hosts_content)


async def write_json_file(hosts_list: List) -> None:
    output_file_path = HOSTS_JSON_PATH
    async with aiofiles.open(output_file_path, "w", encoding="utf-8") as output_fb:
        await output_fb.write(json.dumps(hosts_list))


async def retry_if_result_none(result):
    return result is None


@retry(stop_max_attempt_number=5, retry_on_result=retry_if_result_none)
async def get_ip_from_api(
    amazon_url: str, headers: dict, timeout: int = 5, max_attempts: int = MAX_ATTEMPTS
) -> Optional[str]:
    true_ip = None
    for _ in range(max_attempts):
        try:
            async with ClientSession() as session:
                async with session.get(
                    f"http://ip-api.com/json/{amazon_url}?lang=zh-CN",
                    headers=headers,
                    timeout=timeout,
                ) as res:
                    res = await res.text()

            res = json.loads(res)

            if (
                res["status"] == "success"
                and len(re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", res["query"]))
                == 1
            ):
                true_ip = res["query"]
                break
        except Exception as e:
            logger.error(f"Error querying {amazon_url}: {str(e)}")

    return true_ip


async def query_ip_api(amazon_url: str) -> Optional[str]:
    try:
        # Use Amazon's domain for resolution
        amazon_ips = socket.gethostbyname_ex(amazon_url)
        # Return all IP addresses
        return amazon_ips[2]
    except socket.error as e:
        print(
            f"Error querying {amazon_url} by Socket. Trying to get IP from API: {str(e)}"
        )
        try:
            # Use Amazon's domain for resolution
            c_amazon_ips = await get_ip_from_api(
                amazon_url,
                headers={
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36",
                    "Host": "ip-api.com",
                },
            )
            # Return all IP addresses
            return c_amazon_ips
        except socket.error as e:
            print(f"Error querying {amazon_url} by API: {str(e)}")
            return None


async def process_url(session: any, amazon_url: str, verbose: bool) -> Optional[tuple]:
    try:
        ip = await get_ip(session, amazon_url)
        best_ip = get_best_ip(ip)
        if verbose:
            logger.info(f"Processed {amazon_url}")
        return best_ip, amazon_url
    except Exception as e:
        logger.error(f"Error processing {amazon_url}: {str(e)}")
        return "", amazon_url


async def process_urls(session: any, verbose: bool) -> List[tuple]:
    content_list = []
    tasks = [
        process_url(session, url, verbose) for url in AMAZON_URLS
    ]

    for result in await asyncio.gather(*tasks):
        if result:
            content_list.append(result)

    return content_list


def get_best_ip(ip_list: List[str]) -> str:
    best_ip = ""
    min_ms = PING_TIMEOUT * 1000
    for ip in ip_list:
        ping_result = ping(ip, timeout=PING_TIMEOUT)
        if ping_result.rtt_avg_ms == PING_TIMEOUT * 1000:
            # Timeout, consider IP invalid
            continue
        else:
            if ping_result.rtt_avg_ms < min_ms:
                min_ms = ping_result.rtt_avg_ms
                best_ip = ip
    return best_ip


async def get_ip(session: any, amazon_url: str) -> Optional[str]:
    return await query_ip_api(amazon_url)


async def main(verbose: bool = False) -> None:
    session = ClientSession(connector=TCPConnector(limit=CONCURRENT_REQUESTS))
    start_time = time.time()
    content_list = await process_urls(session, verbose)
    end_time = time.time()

    if not content_list:
        logger.warning("No valid content obtained.")
        await session.close()
        return

    content = "\n".join(
        [
            f'{ip.ljust(30) if ip != "" else "#".ljust(30)}{url}'
            for ip, url in content_list
        ]
    )

    update_time = (
        datetime.utcnow()
        .astimezone(timezone(timedelta(hours=8)))
        .replace(microsecond=0)
        .isoformat()
    )

    hosts_content = HOSTS_TEMPLATE.format(content=content, update_time=update_time)
    has_change = await write_file(hosts_content, update_time)

    if has_change:
        await write_json_file(content_list)

    await session.close()

    if verbose:
        logger.info(hosts_content)
        logger.info(f"End script. Time taken: {end_time - start_time:.2f} seconds.")


if __name__ == "__main__":
    asyncio.run(main(True))
