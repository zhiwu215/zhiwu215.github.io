+++
date = '2026-09-05T11:43:55+08:00'
title = 'Electron Vite搭建react+ts项目'
summary = '使用electron-vite搭建项目'
tags = ['electron-vite']

series=['electron-vite项目搭建']

draft = true

+++

## 搭建项目

官网：

[快速开始 | electron-vite](https://cn.electron-vite.org/guide/#搭建第一个-electron-vite-项目)

![image-20260905114640968](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260905114640968.png)

这里我使用react+ts，所以可以直接**使用模板**：

```bash
pnpm create @quick-start/electron <项目名> --template react
```

![image-20260905115003154](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260905115003154.png)

### 解决ERR_PNPM_IGNORED_BUILDS

详情：[两种方法解决 ERR_PNPM_IGNORED_BUILDS | 知兀的博客](https://zhiwu215.github.io/posts/解决err_pnpm_ignored_builds/)

### 清理默认文件

**保留**

**src\renderer\src\App.tsx**

```tsx
function App(): React.JSX.Element {
  return <></>
}

export default App
```

**删除**

**src/renderer/src/assets**

- electron.svg
- wavy-lines.svg
- main.css
- base.css

**src/renderer/src\/components**

- Versions.tsx

**src/main/src/index.ts**

```typescript
// IPC test
ipcMain.on('ping', () => console.log('pong'))
```

**src/renderer/src/main.tsx**

```diff
import './assets/main.css'
```
