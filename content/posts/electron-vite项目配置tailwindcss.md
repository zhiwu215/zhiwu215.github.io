+++
date = '2026-09-05T13:47:06+08:00'
title = 'Electron Vite项目配置tailwindcss'
summary = '配置tailwindcss'
tags = ['electron', 'electron-vite']

series=['electron-vite项目搭建']

+++

## 官方文档

[Installing Tailwind CSS with Vite - Tailwind CSS](https://tailwindcss.com/docs/installation/using-vite)

![image-20260905133404899](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260905133404899.png)

## 安装依赖

```bash
pnpm add tailwindcss @tailwindcss/vite
```

## 配置vite插件

**electron.vite.config.ts**

> 为什么要@ts-expect-error，查看[解决 Tailwindcss 报错：没有与此调用匹配的重载 | 知兀的博客](https://zhiwu215.github.io/posts/解决tailwindcss报错没有与此调用匹配的重载/)

```diff
import { resolve } from 'path'
import { defineConfig } from 'electron-vite'
import react from '@vitejs/plugin-react'
+import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  main: {},
  preload: {},
  renderer: {
    resolve: {
      alias: {
        '@renderer': resolve('src/renderer/src')
      }
    },
    plugins: [
      react(),
+     // @ts-expect-error
+     tailwindcss()
    ]
  }
})
```

## 导入Tailwind CSS

**src/renderer/src/assets/globals.css**

> 文件名随便

```css
@import "tailwindcss";
```
