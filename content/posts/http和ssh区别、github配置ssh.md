+++
date = '2026-09-22T08:55:56+08:00'

title = 'HTTP和SSH区别、github配置ssh'

summary = '说明HTTP和SSH区别，并为github配置ssh'

tags = ['git', 'github', 'ssh']

+++

## http和ssh有什么区别

![img](https://raw.githubusercontent.com/zhiwu215/blog-img/main/e2207ecb7e294d0282cd1032171eab2a.png)

### 对比

不管是 HTTPS 还是 SSH，传输的代码内容本身是完全相同的，它们的核心区别在于**网络通道和身份认证**

| 维度             | HTTPS 方式 (`https://...`)                                   | SSH 方式 (`git@...`)                                   |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| **认证方式**     | **账号密码 / 网页授权 (Token)**                              | **公钥 + 私钥（非对称加密）**                          |
| **首次使用成本** | **零门槛**，直接复制就能 clone                               | **需要配置**（生成密钥并粘贴到 GitHub）                |
| **日常使用体验** | Windows 会自动弹窗登录并缓存凭据；偶尔 Token 过期需要重新授权 | **极致丝滑**，一旦配好几年内没有任何弹窗提示，静默完成 |
| **网络端口**     | 走 **443 端口**（网页常用端口，全国哪里都能通）              | 走 **22 端口**（部分公司、校园内网可能会屏蔽 22 端口） |
| **公开项目克隆** | 任何人都可以直接下载，无需任何账号                           | 电脑必须有 SSH 环境才能连                              |

**http：**

**第一次需要让你在网页上授权一次确认身份**。现代 Windows 上的 Git 凭据管理器（Git Credential Manager）**会自动帮你把凭据存好**。以后每次敲 git push，Git 都会在后台悄悄向 Windows 的凭据管理器要这个令牌，毫秒级验证通过并直接完成推送。全程没有任何弹窗，也不需要浏览器介入，**体验和 SSH 几乎没有任何区别**

**ssh：**

在电脑本地生成一对钥匙：公钥（相当于给私钥用的锁）和私钥

公钥留在 GitHub 服务器上，每次你连接时，GitHub 拿公钥，你本地用私钥瞬间解开。全程在后台几毫秒完成，不需要经过浏览器

### 为什么还要用ssh

在 **Windows 个人电脑 + 单账号** 的前提下，由于现代 Windows 的 **Git 凭据管理器（GCM）** 做得太好了，**日常使用中 HTTPS 和 SSH 已经几乎感受不到区别，那为什么还要使用ssh？**

**历史原因：**

在过去，GitHub 允许 HTTPS 直接输账号密码。后来为了安全，GitHub 禁用了密码登录，强制要求使用一长串字符的个人访问令牌。 在当时还没有这么完善的凭据管理器时，每次推代码都要翻小本本复制 Token，体验极差

而 SSH 几十年来一直是一次配置、终身免密

**功能强大：**

**多账号管理**

如果你这台电脑同时有：

- 公司工作账号（比如公司内网的 GitLab 或企业 GitHub）
- 个人开源账号（你自己的 GitHub）

如果全用 HTTPS，Windows 凭据管理器很容易串号。 而 SSH 可以给不同账号分别指定不同的密钥文件。Git 会根据你的配置精确匹配，绝对不会串号

**无桌面环境**

在 Windows/Mac 上，HTTPS 第一次可以弹出一个浏览器网页让你点“授权”。

但在 Linux 服务器、Docker 容器、或者用命令行 SSH 远程连接云主机时，是没有浏览器界面的，HTTPS 授权就会变得很繁琐

**自动化部署**

网站自动上线脚本、服务器定时拉取最新代码等场景，都是由机器自动执行的。只需要在 GitHub 仓库里扔一个只读公钥，服务器就能静默拉取代码

## github配置ssh

**密钥生成**

```
ssh-keygen -t ed25519 -C "<你的邮箱>"
```

一直按回车：使用默认路径且不设密码

**默认路径：**

- Windows：C:\Users\你的用户名\.ssh\id_ed25519

![image-20260922090756123](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260922090756123.png)

**复制后添加到github**

```
cat ~/.ssh/id_ed25519.pub
```

复制文件中全部内容后，打开打开浏览器访问 [GitHub SSH Keys 设置页](https://github.com/settings/keys)

点击 New SSH key，Title 随意填写，Key 区域粘贴刚才复制的内容并保存

![img](https://raw.githubusercontent.com/zhiwu215/blog-img/main/a9918a6523274cc5a057191b923df798.png)

测试

```
ssh -T git@github.com
```

![image-20260922092352404](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260922092352404.png)

**第一次使用 SSH 协议连接 GitHub 服务器时，系统就会给出安全确认提示**

问你是否确定要连接这个服务器

`SHA256:...` 开头的内容就是github服务器的指纹，输入 `yes` 并回车后，系统会将 GitHub 的指纹信息保存到你本地电脑的 `~/.ssh/known_hosts` 文件中

最后终端显示的就是欢迎信息了
