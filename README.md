# Amazon_host
*注：* 本项目还处于测试阶段，仅在本机测试通过，如有问题欢迎提 [issues](https://github.com/freysu/amazon_host/issues/new)


## 二、使用方法

下面的地址无需访问 GitHub 即可获取到最新的 hosts 内容：

- 文件：`https://raw.githubusercontent.com/freysu/amazon_host/main/hosts`
- JSON：`https://raw.githubusercontent.com/freysu/amazon_host/main/hosts.json`

### 2.1 手动方式

#### 2.1.1 复制下面的内容

```bash
# Amazon Host Start
#                             a2z.com
#                             aan.amazon.es
#                             aan.amazon.fr
#                             aan.amazon.de
#                             aan.amazon.it
#                             a.media-amazon.com
#                             aax-eu.amazon.de
#                             aax-eu.amazon.es
#                             aax-eu.amazon.fr
#                             aax-eu.amazon.it
#                             amazon-adsystem.com
#                             aax-us-iad.amazon.com
#                             alexa-smart-nudge.amazon.com
#                             amazon.com
#                             amazon.de
#                             amazon.es
#                             af4c2fc8cd0293f914dfc6c3f3b02a7a8.profile.lhr61-p2.cloudfront.net
#                             amazon.fr
#                             api.amazon.com
#                             cloudfront.net
#                             appx.transient.amazon.com
#                             completion.amazon.com
#                             completion.amazon.de
#                             amazon.it
#                             completion.amazon.es
#                             completion.amazon.fr
#                             completion.amazon.it
#                             arcus-uswest.amazon.com
#                             data-na.amazon.com
#                             avs-alexa-16-na.amazon.com
#                             d1f0esyb34c1g2.cloudfront.net
#                             d1lxz4vuik53pc.cloudfront.net
#                             d39x00gckxu2jb.cloudfront.net
#                             dk9ps7goqoeef.cloudfront.net
#                             device-metrics-us-2.amazon.com
#                             device-metrics-us.amazon.com
#                             f.media-amazon.com
#                             dtjsystab5p0r.cloudfront.net
#                             fls-eu.amazon.de
#                             fls-eu.amazon.es
#                             fls-eu.amazon.fr
#                             fls-eu.amazon.it
#                             images-eu.ssl-images-amazon.com
#                             images-fe.ssl-images-amazon.com
#                             media-amazon.com
#                             mag-na.amazon.com
#                             images-na.ssl-images-amazon.com
#                             msh.amazon.com
#                             m.media-amazon.com
#                             ssl-images-amazon.com
#                             prime.amazon.com
#                             fls-na.amazon.com
#                             transient.amazon.com
#                             unagi.amazon.de
#                             unagi.amazon.es
#                             unagi.amazon.fr
#                             prod-1.us-east-1.mdcs.mshop.amazon.dev
#                             unagi-na.amazon.com
#                             unagi.amazon.it
#                             unagi.amazon.com
#                             whoami.akamai.net
#                             www.amazon.com
#                             www.amazon.de
#                             www.amazon.es
#                             www.amazon.fr
#                             www.amazon.it

# Update time: 2024-01-31T18:17:06+08:00
# Update url: https://raw.githubusercontent.com/freysu/amazon_host/main/hosts
# Star me: https://github.com/reysu/amazon_host
# Amazon Host End

```

该内容会自动定时更新， 数据更新时间：2024-01-31T18:17:06+08:00

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
