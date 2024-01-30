import os
import re
import json
import requests
import socket
from datetime import datetime, timezone, timedelta
from typing import Any, Optional, List
from pythonping import ping
from requests_html import HTMLSession
from retry import retry

# Constants and Configuration
GITHUB_URLS = [
        "a.media-amazon.com",
        "a2z.com",
        "aan.amazon.de",
        "aan.amazon.es",
        "aan.amazon.fr",
        "aan.amazon.it",
        "aax-eu.amazon.de",
        "aax-eu.amazon.es",
        "aax-eu.amazon.fr",
        "aax-eu.amazon.it",
        "aax-us-iad.amazon.com",
        "af4c2fc8cd0293f914dfc6c3f3b02a7a8.profile.lhr61-p2.cloudfront.net",
        "alexa-smart-nudge.amazon.com",
        "amazon-adsystem.com",
        "amazon.com",
        "amazon.de",
        "amazon.es",
        "amazon.fr",
        "amazon.it",
        "api.amazon.com",
        "appx.transient.amazon.com",
        "arcus-uswest.amazon.com",
        "avs-alexa-16-na.amazon.com",
        "cloudfront.net",
        "completion.amazon.com",
        "completion.amazon.de",
        "completion.amazon.es",
        "completion.amazon.fr",
        "completion.amazon.it",
        "d1f0esyb34c1g2.cloudfront.net",
        "d1lxz4vuik53pc.cloudfront.net",
        "d39x00gckxu2jb.cloudfront.net",
        "data-na.amazon.com",
        "device-metrics-us-2.amazon.com",
        "device-metrics-us.amazon.com",
        "dk9ps7goqoeef.cloudfront.net",
        "dtjsystab5p0r.cloudfront.net",
        "f.media-amazon.com",
        "fls-eu.amazon.de",
        "fls-eu.amazon.es",
        "fls-eu.amazon.fr",
        "fls-eu.amazon.it",
        "fls-na.amazon.com",
        "images-eu.ssl-images-amazon.com",
        "images-fe.ssl-images-amazon.com",
        "images-na.ssl-images-amazon.com",
        "m.media-amazon.com",
        "mag-na.amazon.com",
        "media-amazon.com",
        "msh.amazon.com",
        "prime.amazon.com",
        "prod-1.us-east-1.mdcs.mshop.amazon.dev",
        "ssl-images-amazon.com",
        "transient.amazon.com",
        "unagi-na.amazon.com",
        "unagi.amazon.com",
        "unagi.amazon.de",
        "unagi.amazon.es",
        "unagi.amazon.fr",
        "unagi.amazon.it",
        "whoami.akamai.net",
        "www.amazon.com",
        "www.amazon.de",
        "www.amazon.es",
        "www.amazon.fr",
        "www.amazon.it"
]


HOSTS_TEMPLATE = """# GitHub520 Host Start
{content}

# Update time: {update_time}
# Update url: https://raw.hellogithub.com/hosts
# Star me: https://github.com/521xueweihan/GitHub520
# GitHub520 Host End\n"""

SCRIPT_DIR = os.path.dirname(__file__)
README_PATH = os.path.join(SCRIPT_DIR, "README.md")
README_TEMPLATE_PATH = os.path.join(SCRIPT_DIR, "README_template.md")
HOSTS_PATH = os.path.join(SCRIPT_DIR, "hosts")
HOSTS_JSON_PATH = os.path.join(SCRIPT_DIR, "hosts.json")


def setup_logging():
    # Set up logging configuration here
    pass


def write_file(hosts_content: str, update_time: str) -> bool:
    output_doc_file_path = README_PATH
    template_path = README_TEMPLATE_PATH
    write_host_file(hosts_content)
    
    if os.path.exists(output_doc_file_path):
        with open(output_doc_file_path, "r") as old_readme_fb:
            old_content = old_readme_fb.read()
            if old_content:
                old_hosts = old_content.split("```bash")[1].split("```")[0].strip()
                old_hosts = old_hosts.split("# Update time:")[0].strip()
                hosts_content_hosts = hosts_content.split("# Update time:")[
                    0].strip()
                if old_hosts == hosts_content_hosts:
                    print("host not change")
                    return False

    with open(template_path, "r") as temp_fb:
        template_str = temp_fb.read()
        hosts_content = template_str.format(hosts_str=hosts_content,
                                            update_time=update_time)
        with open(output_doc_file_path, "w") as output_fb:
            output_fb.write(hosts_content)
    return True


def write_host_file(hosts_content: str) -> None:
    output_file_path = HOSTS_PATH
    with open(output_file_path, "w") as output_fb:
        output_fb.write(hosts_content)


def write_json_file(hosts_list: List) -> None:
    output_file_path = HOSTS_JSON_PATH
    with open(output_file_path, "w") as output_fb:
        json.dump(hosts_list, output_fb)


def getIpFromipapi(site: str) -> Optional[str]:
    '''
    return trueip: None or ip
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'ip-api.com'
    }
    url = f"http://ip-api.com/json/{site}?lang=zh-CN"
    trueip = None
    for i in range(5):
        try:
            res = requests.get(url, headers=headers, timeout=5)
            res = json.loads(res.text)
            if res["status"] == "success" and len(re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", res["query"])) == 1:
                trueip = res["query"]
                break
        except Exception as e:
            print(f"Error querying {site}: {str(e)}")
    return trueip

def getIpFromSocket(site: str) -> Optional[str]:
    try:
        # 使用GitHub的域名进行解析
        github_ips = socket.gethostbyname_ex(site)
        # 返回所有IP地址
        return github_ips[2]
    except socket.error as e:
        print(f"Error query by Socket. Try to getIpFromipapi: {str(e)}")
        try:
            # 使用GitHub的域名进行解析
            c_github_ips = getIpFromipapi(site)
            # 返回所有IP地址
            return c_github_ips
        except socket.error as e:
            print(f"Error querying {site} : {str(e)}")
            return None


def get_best_ip(ip_list: List[str]) -> str:
    ping_timeout = 2
    best_ip = ''
    min_ms = ping_timeout * 1000
    for ip in ip_list:
        ping_result = ping(ip, timeout=ping_timeout)
        if ping_result.rtt_avg_ms == ping_timeout * 1000:
            # Timeout, consider IP invalid
            continue
        else:
            if ping_result.rtt_avg_ms < min_ms:
                min_ms = ping_result.rtt_avg_ms
                best_ip = ip
    return best_ip


@retry(tries=5)
def get_ip(session: Any, github_url: str) -> Optional[str]:
    return getIpFromSocket(github_url)


def process_urls(session: Any, verbose: bool) -> List:
    content_list = []
    for index, github_url in enumerate(GITHUB_URLS):
        try:
            ip = get_ip(session, github_url)
            best_ip = get_best_ip(ip)
            content_list.append((best_ip, github_url,))
            if verbose:
                print(f'process url: {index + 1}/{len(GITHUB_URLS)}')
        except Exception:
            continue
    return content_list


def main(verbose: bool = False) -> None:
    setup_logging()
    session = HTMLSession()
    content_list = process_urls(session, verbose)

    if not content_list:
        return

    # content = "\n".join([f"{ip.ljust(30)}{url}" for ip, url in content_list])
    # content = "\n".join([f"{ip.ljust(30) if ip else '# '.ljust(30)}{url}" for ip, url in content_list])
    content = "\n".join([f"{str(ip).ljust(30) if ip is not None else 'None'.ljust(30)}{url}" for ip, url in content_list])



    update_time = datetime.utcnow().astimezone(
        timezone(timedelta(hours=8))).replace(microsecond=0).isoformat()

    hosts_content = HOSTS_TEMPLATE.format(content=content, update_time=update_time)
    has_change = write_file(hosts_content, update_time)

    if has_change:
        write_json_file(content_list)

    if verbose:
        print(hosts_content)
        print('End script.')


if __name__ == '__main__':
    main(True)
