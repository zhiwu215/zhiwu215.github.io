+++
date = '2026-11-14T10:39:10+08:00'

title = 'Vscode查看和编辑md文档'

summary = '使用vscode安装插件和进行配置，用于查看、编辑markdown文档。'

tags = ['vscode', 'markdown']

+++

## vscode本身就能预览md文档

> vscode的官方文档
>
> [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)
>
> ![image-20261114103935992](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114103935992.png)
>
> ![image-20261114104020110](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114104020110.png)
>
> ![image-20261114104047201](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114104047201.png)

在右上角这个就可以选择显示的方式

还可以设置默认值

![image-20261114104948239](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114104948239.png)

## 个人安装插件

### Markdown All in One

![image-20261115025358442](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261115025358442.png)

**查看「细节」说明：**

**键盘快捷键**：快速切换粗体、斜体、标题等

**目录**：插入目录，并可在保存时自动更新

**列表编辑**：使用 Tab 或退格调整缩进，自动添加有序列表编号

**导出 HTML**

**GitHub 风格 Markdown**：格式化表格

**数学公式**

**自动补全**：补全图片和文件路径、数学函数、引用链接

**其他功能**：把选中的文字转换成链接

> 我个人觉得加粗、标题级别设置、列表缩进等的快捷键很好用
>
> 所以安装这个插件

### Markdown Preview Enhanced

这是「细节」里的说明

![image-20261115031845279](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261115031845279.png)

可以在「细节」里面，直接跳转到[中文文档](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/)具体查看功能

![image-20261114105628114](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114105628114.png)

> 我个人需要看mermaid图和plantuml图这些，所以用这个插件预览很方便

## 可选插件

### markdownlint

用来检查 Markdown 文档的格式规范和风格

> 不过我不喜欢用，因为它会检查格式规范，有时候我就想要按照自己写法来，而不是写错了

![image-20261115033332837](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261115033332837.png)

## 标点位置导致的渲染问题

VSCode内置预览使用的是`markdown-it`

2017年就提交过[issue](https://github.com/markdown-it/markdown-it/issues/340)了

如图是issue中Demo的链接：

![image-20261114123916919](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114123916919.png)

**中文标点不能放在斜体、加粗等语法范围最后**，不然渲染会有问题

**这只是vscode上游的问题**，用其他的md笔记软件，不会有这个问题

## 图片存放路径

### 默认

如图可以看到，粘贴图片，图片自动放在了和文档同级的目录下

![image-20261114125535140](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114125535140.png)

### 修改路径

> 官方文档：
>
> [Markdown 和 Visual Studio 代码 --- Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown#_inserting-images-and-links-to-files)
>
> ![image-20261114130022971](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114130022971.png)

我把图片放到当前 Markdown 文件旁边的 `imgs` 文件夹里

![image-20261114131908659](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114131908659.png)

## plantuml图

> 文档里面演示：
>
> [图像](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/diagrams?id=plantuml)
>
> ![image-20261114114020325](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114114020325.png)

### 报错

但实际使用会报错

![image-20261114114116320](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114114116320.png)

原因：

[官方日志](https://github.com/shd101wyy/vscode-markdown-preview-enhanced/blob/develop/CHANGELOG.md)

从 **0.7.0** 起，插件移除了原来内置的 `plantuml.jar`，需要用户自行提供，并配置 `markdown-preview-enhanced.plantumlJarPath`

![image-20261114113932410](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114113932410.png)

### 安装plantuml.jar

[plantuml.jar下载地址](https://plantuml.com/zh/download)

> 我按官方文档说GPL版本提供了全面的功能
>
> 那我就下载这个版本吧

![image-20261114114910728](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114114910728.png)

下载完成后，放在合适的地方

![image-20261114115825088](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114115825088.png)

[文档](https://plantuml.com/zh/starting)说明本地使用需要前置条件

![image-20261114115603096](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114115603096.png)

### 配置vscode

在日志里面已经说了，在 VSCode 设置里设置 `markdown-preview-enhanced.plantumlJarPath` 选项

![image-20261114120418435](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114120418435.png)

### 可以显示但DTO禁止

![image-20261114120831181](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114120831181.png)

已经可以正常显示了，但DOT图不行，这是插件自己禁止的

如果点击这个链接，可以看到具体的issue

![image-20261114120946647](https://raw.githubusercontent.com/zhiwu215/blog-img/main/image-20261114120946647.png)
