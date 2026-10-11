+++
date = '2026-10-11T18:08:06+08:00'

title = 'VitePress部署项目的说明文档'

summary = 'VitePress部署项目的说明文档'

tags = ['VitePress']

+++

## VitePress是什么

官方文档：

[VitePress 是什么？ | VitePress](https://vitepress.dev/zh/guide/what-is-vitepress)

VitePress 是一个静态站点生成器 (SSG)，可以用来部署文档，比如Vite、Pinia等的说明文档，也可以用来部署博客等等

> 不过博客我使用hugo部署
>
> 因为经常看些Vite、Vue、PPinia的说明文档，所以我也决定使用VitePress来部署项目的说明文档

![image-20261011181103249](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261011181103249.png)

## 使用场景

最常见的是：**独立新建一个专门的文档仓库**

比如官方项目自己创建文档：

**React**

- **核心源码仓库**：https://github.com/facebook/react
- **独立文档仓库**：https://github.com/reactjs/react.dev （专门用 Next.js 搭建的文档工程）
- **在线文档站点**：https://react.dev/

**Vue.js**

- **核心源码仓库**：https://github.com/vuejs/core

- **独立文档仓库**：https://github.com/vuejs/docs （专门用 VitePress 搭建的文档工程）

- **中文文档独立仓库**：https://github.com/vuejs-translations/docs-zh-cn
- **在线文档站点**：https://cn.vuejs.org/

比如给第三方项目创建文档：

**《Rust 圣经》（Rust 语言中文教程）**

- **原项目代码**：https://github.com/rust-lang/rust （Rust 官方编译器）
- **第三方独立文档仓库**：https://github.com/sunface/rust-course （国内开发者独立建立的中文文档库）
- **在线文档站点**：https://course.rs/

**《Docker 从入门到实践》**

- **原项目代码**：https://github.com/moby/moby （Docker 核心源码，属于 Docker 公司）
- **第三方独立文档仓库**：https://github.com/yeasy/docker_practice （社区独立搭建的中文文档与实践指南）
- **在线文档站点**：[Docker 从入门到实践](https://yeasy.gitbook.io/docker_practice)

## 快速开始

### 创建仓库

创建一个空白的public仓库

> 名字可以修改，所以不用担心取名问题

### 初始化VitePress

> 官方文档：
>
> [快速开始 | VitePress](https://vitepress.dev/zh/guide/getting-started)
>
> 第一个命令是安装依赖
>
> 第二个命令是创建模板骨架
>
> ![image-20261011182240542](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261011182240542.png)

```bash
# 1. 新建并进入工程目录
mkdir <仓库名>
cd <仓库名>

# 2. 初始化工程并安装 VitePress
pnpm init
pnpm add -D vitepress

# 3. 运行交互式模板初始化向导
pnpm vitepress init
```

### git忽略文件

```
# 依赖
node_modules

# VitePress 构建产物与本地缓存
.vitepress/dist
.vitepress/cache
```

### 修改配置文件

官方文档：

[部署 VitePress 站点 | VitePress](https://vitepress.dev/zh/guide/deploy#setting-a-public-base-path)

![image-20261011185622468](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261011185622468.png)

GitHub Pages 分配给你的二级目录是 `https://<你的用户名>.github.io/<仓库名>/`

因此必须在配置里加上 `base: '/<你的仓库名>/'`，否则部署后静态资源会全部 404

**.vitepress/config.mts**

```diff
import { defineConfig } from 'vitepress'

export default defineConfig({
  
+ base: '<必须与你的 GitHub 仓库名一致（前后加斜杠）>',

  title: '标题',
  description: '描述',
  lang: 'zh-CN',

  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '快速开始', link: '/guide/quick-start' },
      { text: '上游源码', link: 'https://github.com/purerosefallen/koishipro-core.js' }
    ],
    sidebar: [
      {
        text: '指引',
        items: [
          { text: '快速上手', link: '/guide/quick-start' },
          { text: '录像单步推演', link: '/guide/replay' }
        ]
      }
    ]
  }
})
```

### GitHub Actions自动部署脚本

官方文档：

[部署 VitePress 站点 | VitePress](https://vitepress.dev/zh/guide/deploy#github-pages)

![image-20261011190042916](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261011190042916.png)

```diff
# 构建 VitePress 站点并将其部署到 GitHub Pages 的示例工作流程
#
name: Deploy VitePress site to Pages

on:
  # 在针对 `main` 分支的推送上运行。如果你
  # 使用 `master` 分支作为默认分支，请将其更改为 `master`
  push:
    branches: [main]

  # 允许你从 Actions 选项卡手动运行此工作流程
  workflow_dispatch:

# 设置 GITHUB_TOKEN 的权限，以允许部署到 GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# 只允许同时进行一次部署，跳过正在运行和最新队列之间的运行队列
# 但是，不要取消正在进行的运行，因为我们希望允许这些生产部署完成
concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  # 构建工作
  build:
    runs-on: ubuntu-latest
    steps:
       - name: Checkout
         uses: actions/checkout@v5
         with:
           fetch-depth: 0 # 如果未启用 lastUpdated，则不需要
-      # - uses: pnpm/action-setup@v4 # 如果使用 pnpm，请取消此区域注释
-      #   with:
-      #     version: 9
+      # 配置删除就行，能自动去读取 package.json 的版本
       # - uses: oven-sh/setup-bun@v1 # 如果使用 Bun，请取消注释
       - name: Setup Node
         uses: actions/setup-node@v6
         with:
           node-version: 24
-          cache: npm # 或 pnpm / yarn
+          cache: pnpm # 或 pnpm / yarn
       - name: Setup Pages
         uses: actions/configure-pages@v4
       - name: Install dependencies
-        run: npm ci # 或 pnpm install / yarn install / bun install
+        run: pnpm install # 或 pnpm install / yarn install / bun install
       - name: Build with VitePress
-        run: npm run docs:build # 或 pnpm docs:build / yarn docs:build / bun run docs:build
+        run: pnpm run docs:build # 或 pnpm docs:build / yarn docs:build / bun run docs:build
       - name: Upload artifact
         uses: actions/upload-pages-artifact@v3
         with:
-          path: docs/.vitepress/dist
+          # 创建模板时，vitepress被我配置在根目录了
+          path: .vitepress/dist

  # 部署工作
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    needs: build
    runs-on: ubuntu-latest
    name: Deploy
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 推送到 GitHub 并一键开启

执行git命令push项目

推送完成后：

GitHub 仓库的 **Settings** -> **Pages**，将 **Source** 选为 **GitHub Actions**，等待流水线跑完即可在线访问你的文档网站，访问网址是： `https://<你的用户名>.github.io/<仓库名>/`
