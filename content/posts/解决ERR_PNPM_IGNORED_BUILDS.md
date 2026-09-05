+++
date = '2026-09-05T12:57:51+08:00'
title = '两种方法解决ERR_PNPM_IGNORED_BUILDS'
summary = '解决pnpm install时，ERR_PNPM_IGNORED_BUILDS的报错'
tags = ['pnpm', '包管理器']

+++

## 为什么会报错

![image-20260905130150411](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260905130150411.png)

官方文档：

[Build Settings | pnpm](https://pnpm.io/settings/build#strictdepbuilds)

`strictDepBuilds`默认为true，一旦存在未审核的构建脚本{{<marginnote>}}**构建脚本（build scripts）**，就是 npm 包生命周期脚本里的： `preinstall`、`install`、`postinstall`：

它不是你手动敲命令运行的脚本。

它是包被下载完之后，npm/pnpm 自动、悄悄执行的一段代码{{</marginnote>}}，安装直接报错终止

这是一种安全措施，防止恶意包在安装时执行危险代码

![image-20260905120307735](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260905120307735.png)

## 方法一：交互式审批

**放行**

```bash
pnpm approve-builds
```

选中需要放行的包，这条命令会自动生成 `pnpm‑workspace.yaml` 文件，写入白名单

![image-20260905120900105](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260905120900105.png)

**运行**

```bash
pnpm dev
```

pnpm 在执行 dev 脚本之前，检测 lock‑file 有缺失的构建任务，在启动脚本前自动补发执行了被拦截的构建脚本

![image-20260905121307479](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260905121307479.png)

## 方法二：手动新建 `pnpm‑workspace.yaml`

> 官方文档：
>
> [Build Settings | pnpm](https://pnpm.io/zh/settings/build#allowbuilds)
>
> ![image-20260905130643977](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260905130643977.png)

**创建或修改`pnpm-workspace.yaml`**

在项目根目录创建或修改 `pnpm-workspace.yaml` 文件，添加 `allowBuilds` 配置：

- 不带版本（全局放行）

- 指定版本（精准放行）

```bash
allowBuilds:
  <需要放行的包>: true
  <需要放行的包@版本>: true
```

**运行**

```bash
pnpm dev
```
