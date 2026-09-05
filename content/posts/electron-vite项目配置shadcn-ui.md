+++
date = '2026-09-05T18:16:45+08:00'

title = 'Electron Vite项目配置shadcn/ui'

summary = '配置shadcn/ui'

tags = ['electron-vite', 'shadcn/ui']

series=['electron-vite项目搭建']

+++

## 手动安装

官网：

[Installation - shadcn/ui](https://ui.shadcn.com/docs/installation#choose-your-framework)

![image-20260905182718557](https://cdn.jsdelivr.net/gh/zhiwu215/blog-img/image-20260905182718557.png)

![image-20260905182813628](https://cdn.jsdelivr.net/gh/zhiwu215/blog-img/image-20260905182813628.png)

### 安装tailwindcss

详情：[Electron Vite 项目配置 tailwindcss | 知兀的博客](https://zhiwu215.github.io/posts/electron-vite项目配置tailwindcss/)

### 安装依赖

```bash
pnpm add shadcn class-variance-authority cn lucide-react tw-animate-css
```

### 不设置别名，用默认的

文档第三步是配置别名，我们这是electron-vite项目，不设置：

- 普通纯前端 Vite 项目只有一套代码，@直接映射src很方便
- 但 Electron‑vite 是三进程架构：Main 主进程 + Preload 预加载 + Renderer 渲染进程，三套代码放在同一个仓库根目录，共享一份根tsconfig.json

![image-20260905183418117](https://cdn.jsdelivr.net/gh/zhiwu215/blog-img/image-20260905183418117.png)

### 配置style

![image-20260905183454530](https://cdn.jsdelivr.net/gh/zhiwu215/blog-img/image-20260905183454530.png)

和之前配置的tailwind css样式文件放在一起

![image-20260905183709707](https://cdn.jsdelivr.net/gh/zhiwu215/blog-img/image-20260905183709707.png)

### 添加lib/utils.ts

**src/renderer/src/lib/utils.ts**

![image-20260905184016180](https://cdn.jsdelivr.net/gh/zhiwu215/blog-img/image-20260905184016180.png)

### 创建components.json文件

![image-20260905184010581](https://cdn.jsdelivr.net/gh/zhiwu215/blog-img/image-20260905184010581.png)

官方文档要求根目录下创建文件

但因为使用electron-vite，渲染进程在`src/renderer/src`下，而且已经配置了别名@renderer，所以在根目录下创建后要统一修改

```diff
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "base-nova",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "",
-    "css": "src/styles/globals.css",
+    "css": "@renderer/assets/globals.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
-   "components": "@/components",
-    "utils": "@/lib/utils",
-    "ui": "@/components/ui",
-    "lib": "@/lib",
-    "hooks": "@/hooks"
+    "components": "@renderer/components",
+    "utils": "@renderer/lib/utils",
+    "ui": "@renderer/components/ui",
+    "lib": "@renderer/lib",
+    "hooks": "@renderer/hooks"
  },
  "iconLibrary": "lucide"
}
```

### 添加组件

官方文档下选择Manual，最后就能添加组件了

![image-20260905191649052](https://cdn.jsdelivr.net/gh/zhiwu215/blog-img/image-20260905191649052.png)
