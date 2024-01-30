# Amazon_host
*注：* 本项目还处于测试阶段，仅在本机测试通过，如有问题欢迎提 [issues](https://github.com/freysu/amazon_host/issues/new)


## 二、使用方法

下面的地址无需访问 GitHub 即可获取到最新的 hosts 内容：

- 文件：`https://raw.githubusercontent.com/freysu/amazon_host/main/hosts`
- JSON：`https://raw.githubusercontent.com/freysu/amazon_host/main/hosts.json`

### 2.1 手动方式

#### 2.1.1 复制下面的内容

```bash
# GitHub520 Host Start
23.45.180.211                 a.media-amazon.com
#                             a2z.com
176.32.110.78                 aan.amazon.de
54.239.32.31                  aan.amazon.es
176.32.109.33                 aan.amazon.fr
176.32.110.212                aan.amazon.it
52.95.119.2                   aax-eu.amazon.de
52.95.119.2                   aax-eu.amazon.es
52.95.119.2                   aax-eu.amazon.fr
52.95.119.2                   aax-eu.amazon.it
209.54.177.41                 aax-us-iad.amazon.com
216.137.34.45                 af4c2fc8cd0293f914dfc6c3f3b02a7a8.profile.lhr61-p2.cloudfront.net
#                             alexa-smart-nudge.amazon.com
#                             amazon-adsystem.com
54.239.28.85                  amazon.com
52.95.120.34                  amazon.de
52.95.120.38                  amazon.es
54.239.33.91                  amazon.fr
52.95.120.36                  amazon.it
52.119.198.101                api.amazon.com
52.94.234.30                  appx.transient.amazon.com
#                             arcus-uswest.amazon.com
#                             avs-alexa-16-na.amazon.com
#                             cloudfront.net
#                             completion.amazon.com
#                             completion.amazon.de
#                             completion.amazon.es
#                             completion.amazon.fr
#                             completion.amazon.it
18.67.66.200                  d1f0esyb34c1g2.cloudfront.net
18.238.50.45                  d1lxz4vuik53pc.cloudfront.net
13.32.207.224                 d39x00gckxu2jb.cloudfront.net
18.154.235.87                 data-na.amazon.com
#                             device-metrics-us-2.amazon.com
#                             device-metrics-us.amazon.com
18.67.83.222                  dk9ps7goqoeef.cloudfront.net
108.138.82.219                dtjsystab5p0r.cloudfront.net
151.101.65.16                 f.media-amazon.com
#                             fls-eu.amazon.de
#                             fls-eu.amazon.es
#                             fls-eu.amazon.fr
#                             fls-eu.amazon.it
#                             fls-na.amazon.com
3.162.111.204                 images-eu.ssl-images-amazon.com
18.67.83.222                  images-fe.ssl-images-amazon.com
18.154.233.226                images-na.ssl-images-amazon.com
18.160.38.195                 m.media-amazon.com
#                             mag-na.amazon.com
#                             media-amazon.com
52.46.128.80                  msh.amazon.com
209.54.176.231                prime.amazon.com
#                             prod-1.us-east-1.mdcs.mshop.amazon.dev
#                             ssl-images-amazon.com
52.94.226.161                 transient.amazon.com
52.94.235.74                  unagi-na.amazon.com
52.94.235.74                  unagi.amazon.com
67.220.224.106                unagi.amazon.de
67.220.228.134                unagi.amazon.es
52.95.127.127                 unagi.amazon.fr
67.220.228.178                unagi.amazon.it
172.253.195.207               whoami.akamai.net
173.222.168.196               www.amazon.com
18.160.14.91                  www.amazon.de
23.202.154.79                 www.amazon.es
23.202.154.78                 www.amazon.fr
23.202.154.80                 www.amazon.it

# Update time: 2024-01-30T20:19:40+08:00
# Update url: https://raw.githubusercontent.com/freysu/amazon_host/main/hosts
# Star me: https://github.com/freysu/amazon_host
# GitHub520 Host End

```

该内容会自动定时更新， 数据更新时间：2024-01-30T20:19:40+08:00

#### 2.1.2 修改 hosts 文件

hosts 文件在每个系统的位置不一，详情如下：
- Windows 系统：`C:\Windows\System32\drivers\etc\hosts`
- Linux 系统：`/etc/hosts`
- Mac（苹果电脑）系统：`/etc/hosts`
- Android（安卓）系统：`/system/etc/hosts`
- iPhone（iOS）系统：`/etc/hosts`

修改方法，把第一步的内容复制到文本末尾：

1. Windows 使用记事本。
2. Linux、Mac 使用 Root 权限：`sudo vi /etc/hosts`。
3. iPhone、iPad 须越狱、Android 必须要 root。

#### 2.1.3 激活生效
大部分情况下是直接生效，如未生效可尝试下面的办法，刷新 DNS：

1. Windows：在 CMD 窗口输入：`ipconfig /flushdns`

2. Linux 命令：`sudo nscd restart`，如报错则须安装：`sudo apt install nscd` 或 `sudo /etc/init.d/nscd restart`

3. Mac 命令：`sudo killall -HUP mDNSResponder`

**Tips：** 上述方法无效可以尝试重启机器。

### 2.2 自动方式（SwitchHosts）

**Tip**：推荐 [SwitchHosts](https://github.com/oldj/SwitchHosts) 工具管理 hosts

以 SwitchHosts 为例，看一下怎么使用的，配置参考下面：

- Hosts 类型: `Remote`

- Hosts 标题: 随意

- URL: `https://raw.githubusercontent.com/freysu/amazon_host/main/hosts`

- 自动刷新: 最好选 `1 小时`


## 声明
<a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh"><img alt="知识共享许可协议" style="border-width: 0" src="https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png"></a><br>本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh">署名-非商业性使用-禁止演绎 4.0 国际</a> 进行许可。
