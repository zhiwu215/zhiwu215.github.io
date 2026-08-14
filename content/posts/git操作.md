+++
date = '2026-08-14T17:13:45+08:00'
title = 'Git操作'
summary = '这里演示了一系列场景下，git的操作，包含命令和vscode可视化界面'
tags = ['git','vscode']

+++

# 功能分支合并主分支（保持线性历史）

**1.保存当前修改**

 在切换分支或变基前，必须确保工作区是干净的，否则 Git 会阻止你进行高风险操作

```bash
git add .
git commit -m "feat: xxx"
```

**2.变基到主分支 (Rebase)**

如果你的 `main` 分支没有任何新的提交（没动过），你直接切换回 `main` 分支并执行merge，**Git 默认就会直接触发 Fast-forward（快进）合并**

先 `rebase` 再 `merge`，是一种在团队协作里养成的“标准防御性习惯”

```bash
# 当前处于功能分支
git rebase main
```

**3.切换回主分支快进合并** 

**快进合并 (Fast-forward Merge)：** 因为已经完成了变基对齐，此时合并就像快进录像带一样，直接把 `main` 指针移动到最新提交，**绝对不会产生多余的 Merge Commit 节点**。

```bash
git switch main
git merge <你的功能分支名>
```

**4.清理开发分支**

```bash
git branch -d <你的功能分支名>
```

