+++
date = '2026-09-05T14:53:35+08:00'

title = 'Tailwindcss报错：没有与此调用匹配的重载'

summary = '环境：electron-vite安装tailwindcss。报错：没有与此调用匹配的重载'

tags = ['tailwindcss']

draft = true

+++

## 报错

背景：使用electron-vite构建项目，然后安装tailwindcss，在`electron.vite.config.ts`中配置插件

![image-20260905142429766](../../../blog-img/image-20260905142429766.png)

## 类似issue

tailwindcss[具体issue](https://github.com/tailwindlabs/tailwindcss/issues/18802)

这个issue的作者使用SolidStart框架，然后安装@tailwindcss/vite：框架内部自带了一套 Vite 体系，而外部新安装的插件自带了另一套 Vite 体系

![image-20260905150712623](../../../blog-img/image-20260905150712623.png)

但我的项目中

**`Found 1 version of vite`** （全工程只找到了 **1** 个版本的 vite，那就是顶部的 **`7.3.6`**）

**`Found 1 version of rollup`** （全工程也只有 **1** 个版本的 rollup，那就是 **`4.63.1`**）

![image-20260905150557756](../../../blog-img/image-20260905150557756.png)

## 我的报错消息

> 把关键的地方已经加粗标记

没有与此调用匹配的重载。
  最后一个重载给出了以下错误。
    不能将类型“Plugin<any>[]”分配给类型“PluginOption”。
      不能将类型“Plugin<any>[]”分配给类型“PluginOption[]”。
        不能将类型“Plugin<any>”分配给类型“PluginOption”。
          不能将类型“import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.2_46041a9d4deccce9f9aaf674d7cdda12/node_modules/vite/dist/node/index").Plugin<any>”分配给类型“import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.20.1_jiti@2.7.0/node_modules/vite/dist/node/index").Plugin<any>”。
            属性“hotUpdate”的类型不兼容。
              类型“import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup").ObjectHook<(this: import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup").MinimalPluginContext & { ...; }, options: import("D:/Code/Demo/electron-vite-demo/nod...”无法分配给类型“import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup").ObjectHook<(this: import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup").MinimalPluginContext & { ...; }, options: import("D:/Code/Demo/electron-vite-demo/nod...”。存在具有此名称的两种不同类型，但它们是不相关的。
                不能将类型“(this: MinimalPluginContext & { environment: DevEnvironment; }, options: HotUpdateOptions) => void | EnvironmentModuleNode[] | Promise<...>”分配给类型“ObjectHook<(this: MinimalPluginContext & { environment: DevEnvironment; }, options: HotUpdateOptions) => void | EnvironmentModuleNode[] | Promise<...>> | undefined”。
                  不能将类型“(this: import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup").MinimalPluginContext & { ...; }, options: import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.2_46041a9d4deccce9f9aaf674d7cdda12/node_modules/vite/dist/node/index").HotUp...”分配给类型“(this: import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup").MinimalPluginContext & { ...; }, options: import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.20.1_jiti@2.7.0/node_modules/vite/dist/node/index").HotUpdateOptions) => voi...”。
                    每个签名的 "this" 类型不兼容。
                      不能将类型“import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup").MinimalPluginContext & { environment: import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.20.1_jiti@2.7.0/node_modules/vite/dist/node/index").DevEnvironment; }”分配给类型“import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup").MinimalPluginContext & { environment: import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.2_46041a9d4deccce9f9aaf674d7cdda12/node_modules/vite/dist/node/index").DevEnvironment; }”。
                        不能将类型“MinimalPluginContext & { environment: DevEnvironment; }”分配给类型“{ environment: DevEnvironment; }”。
                          在这些类型中，"environment.pluginContainer" 的类型不兼容。
                            不能将类型“EnvironmentPluginContainer\<import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/**vite@7.3.6_@types+node@22.20.1_jiti@2.7.0**/node_modules/vite/dist/node/index").DevEnvironment>”分配给类型“EnvironmentPluginContainer\<import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/**vite@7.3.6_@types+node@22.2_46041a9d4deccce9f9aaf674d7cdda12**/node_modules/vite/dist/node/index").DevEnvironment>”。
                              **类型具有私有属性“_pluginContextMap”的单独声明**。

## 产生原因

> pnpm官方文档：
>
> [How peers are resolved | pnpm](https://pnpm.io/how-peers-are-resolved)
>
> 如果一个包所处的伴生依赖（peer）环境稍有差异，pnpm 就会在 `.pnpm` 下为它各建一个专属的隔离文件夹

流程：

**刚创建项目**

- 刚初始化的 `electron-vite` 模板非常干净，环境里只有 ESLint 带来的 `jiti`
- 此时 Vite 环境里只有 `node` 和 `jiti`
- pnpm 便给它建了环境 A：`vite@7.3.6_@types+node@22.20.1_jiti@2.7.0`

**安装tailwind css**

- 执行 `pnpm add tailwindcss @tailwindcss/vite` 时： **Tailwind CSS v4 的底层核心编译引擎正是 `lightningcss`** 它顺带把 `lightningcss@1.32.0` 安装进了项目
- 此时对Vite来说是个全新的环境，所以pnpm把三者算成了一串新哈希，为它创建了环境 B：`vite@7.3.6_@types+node@22.2_46041a9d...`

同一个包由于包管理器安装成了两份物理文件，导致私有属性跨文件比对失败，引发报错

## 解决

- 在插件上方加上 `// @ts-expect-error` 

- 或直接断言 `tailwindcss() as any` 

这属于纯构建期的类型假阳性报警，完全不影响项目运行与打包
