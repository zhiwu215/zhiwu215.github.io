+++
date = '2026-08-30T10:54:18+08:00'
title = '解决claude code外接大模型使用WebFetch的问题'
summary = '解决Unable to verify if domain xxx is safe to fetch. This may be due to network restrictions or enterprise security policies blocking claude.ai.'
tags = ['claude code', 'agent']

+++

## 报错

![image-20260830105836214](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260830105836214.png)

## 原因

### anthropic-sdk

首先看[anthropic-sdk](https://github.com/anthropics/anthropic-sdk-typescript/tree/main)

可以看到web_search和web_fetch这两个内置工具都是服务端工具，所以它们的执行都依赖 Anthropic 服务端

![image-20260830111437074](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260830111437074.png)

### WebFetch工具

在sdk中，web_search和web_fetch都是服务端工具

但是，在泄露的claude code源码中：

- WebSearch，使用了 SDK 中定义的服务端 web_search
- WebFetch，自己用 axios 实现，属于客户端

**既然如此，为什么WebFetch工具还会报错？**

参考这个[知乎文章](https://zhuanlan.zhihu.com/p/2012819798686454483)下的评论：

Claude Code 的 WebFetch 在发起实际 HTTP 请求前，会先向 claude.ai/ 发送域名安全预检请求。claude.ai 前面部署了 Cloudflare Bot Protection，从 headless CLI 发出的请求会被 Cloudflare 返回 403 JavaScript challenge，而 CLI 环境无法执行 JS，所以预检永远失败。**错误提示里说的 "network restrictions" 其实具有误导性——真正卡住的是 Anthropic 自己 CDN 上的 Cloudflare**

> **官方文档：**
>
> [数据使用 - Claude Code Docs](https://code.claude.com/docs/zh-CN/data-usage#webfetch-domain-safety-check)
>
> ![image-20260830135110887](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260830135110887.png)

## 解决

> 官方文档：
>
> [Claude Code 设置 - Claude Code Docs](https://code.claude.com/docs/zh-CN/settings#available-settings)
>
> ![image-20260830135356568](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260830135356568.png)

**~/.claude/settings.json**

这个配置可以跳过这一步预检

{{< highlight json "linenos=false, hl_lines=3" >}}
{
  "autoUpdatesChannel": "latest",
  "skipWebFetchPreflight": true,
  "env": {
    ...
  }
}
{{< /highlight >}}
