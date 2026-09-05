+++
date = '2026-09-05T15:49:57+08:00'
title = 'Vscode问题面板的报错查看'
summary = ''
tags = ['debug', 'vscode']

+++

# 界面

在问题面板，点击报错，会有**复制**和复制消息两个选项

![image-20260905155710437](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20260905155710437.png)

# 「复制」的内容

> 下面就是内容，我对字段加粗处理，方便查看，原本是没有的

[{
   **"resource"**: "/d:/Code/Demo/electron-vite-demo/electron.vite.config.ts",
   **"owner":** "typescript",
   **"code"**: "2769",
   **"severity"**: 8,
   **"message":** "没有与此调用匹配的重载。\n  最后一个重载给出了以下错误。\n   不能将类型“Plugin<any>[]”分配给类型“PluginOption”。\n    不能将类型“Plugin<any>[]”分配给类型“PluginOption[]”。\n     不能将类型“Plugin<any>”分配给类型“PluginOption”。\n      不能将类型“import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.2_46041a9d4deccce9f9aaf674d7cdda12/node_modules/vite/dist/node/index\").Plugin<any>”分配给类型“import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.20.1_jiti@2.7.0/node_modules/vite/dist/node/index\").Plugin<any>”。\n       属性“hotUpdate”的类型不兼容。\n        类型“import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup\").ObjectHook<(this: import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup\").MinimalPluginContext & { ...; }, options: import(\"D:/Code/Demo/electron-vite-demo/nod...”无法分配给类型“import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup\").ObjectHook<(this: import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup\").MinimalPluginContext & { ...; }, options: import(\"D:/Code/Demo/electron-vite-demo/nod...”。存在具有此名称的两种不同类型，但它们是不相关的。\n         不能将类型“(this: MinimalPluginContext & { environment: DevEnvironment; }, options: HotUpdateOptions) => void | EnvironmentModuleNode[] | Promise<...>”分配给类型“ObjectHook<(this: MinimalPluginContext & { environment: DevEnvironment; }, options: HotUpdateOptions) => void | EnvironmentModuleNode[] | Promise<...>> | undefined”。\n          不能将类型“(this: import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup\").MinimalPluginContext & { ...; }, options: import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.2_46041a9d4deccce9f9aaf674d7cdda12/node_modules/vite/dist/node/index\").HotUp...”分配给类型“(this: import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup\").MinimalPluginContext & { ...; }, options: import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.20.1_jiti@2.7.0/node_modules/vite/dist/node/index\").HotUpdateOptions) => voi...”。\n           每个签名的 \"this\" 类型不兼容。\n            不能将类型“import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup\").MinimalPluginContext & { environment: import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.20.1_jiti@2.7.0/node_modules/vite/dist/node/index\").DevEnvironment; }”分配给类型“import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/rollup@4.63.1/node_modules/rollup/dist/rollup\").MinimalPluginContext & { environment: import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.2_46041a9d4deccce9f9aaf674d7cdda12/node_modules/vite/dist/node/index\").DevEnvironment; }”。\n             不能将类型“MinimalPluginContext & { environment: DevEnvironment; }”分配给类型“{ environment: DevEnvironment; }”。\n              在这些类型中，\"environment.pluginContainer\" 的类型不兼容。\n               不能将类型“EnvironmentPluginContainer<import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.20.1_jiti@2.7.0/node_modules/vite/dist/node/index\").DevEnvironment>”分配给类型“EnvironmentPluginContainer<import(\"D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.2_46041a9d4deccce9f9aaf674d7cdda12/node_modules/vite/dist/node/index\").DevEnvironment>”。\n                类型具有私有属性“_pluginContextMap”的单独声明。",
   **"source"**: "ts",
   **"startLineNumber"**: 17,
   **"startColumn"**: 7,
   **"endLineNumber"**: 17,
   **"endColumn"**: 20,
   **"relatedInformation"**: [
     {
       "startLineNumber": 118,
       "startColumn": 18,
       "endLineNumber": 118,
       "endColumn": 30,
       "message": "在此处声明最后一个重载。",
       "resource": "/D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/electron-vite@5.0.0_support_8fbe30fbe1a2ef11377a687dfa84a1af/node_modules/electron-vite/dist/index.d.ts"
     }
   ],
   **"origin"**: "extHost1"
 }]

# 「复制消息」的内容

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
               不能将类型“EnvironmentPluginContainer\<import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.20.1_jiti@2.7.0/node_modules/vite/dist/node/index").DevEnvironment>”分配给类型“EnvironmentPluginContainer<import("D:/Code/Demo/electron-vite-demo/node_modules/.pnpm/vite@7.3.6_@types+node@22.2_46041a9d4deccce9f9aaf674d7cdda12/node_modules/vite/dist/node/index").DevEnvironment>”。
                类型具有私有属性“_pluginContextMap”的单独声明。

# 总结

「复制」复制的是这个报错完整的内容，包括resource，owner，code等等各种字段

这个json是完整的，表明了在vscode里这个报错的完整格式

「复制消息」实际是复制完整的这个json的message里的内容，也就是报错的信息

**所以一般复制消息看报错就可以了**

1. 第 1 行：结论
2. 中间：推导过程
3. 最后 1 行：真凶
