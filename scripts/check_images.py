import os
import re
import sys

# 兼容 Windows 控制台 UTF-8 输出
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def scan_markdown_file(file_path):
    """扫描单个 Markdown 文件中的图片情况"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"❌ 无法读取文件 {file_path}: {e}")
        return None

    img_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
    html_img_pattern = re.compile(r'<img[^>]+src=["\'](.*?)["\']')

    remote_count = 0
    local_lines = []

    for line_num, line in enumerate(lines, start=1):
        # 1. 检查 Markdown 图片语法 ![alt](url)
        for match in img_pattern.finditer(line):
            src = match.group(2).strip().split()[0]
            if src.startswith(('http://', 'https://', '//', 'data:')):
                remote_count += 1
            else:
                local_lines.append(line_num)

        # 2. 检查 HTML <img> 语法
        for match in html_img_pattern.finditer(line):
            src = match.group(1).strip().split()[0]
            if src.startswith(('http://', 'https://', '//', 'data:')):
                remote_count += 1
            else:
                local_lines.append(line_num)

    total_count = remote_count + len(local_lines)
    return {
        "file_name": os.path.basename(file_path),
        "file_path": file_path,
        "total": total_count,
        "remote": remote_count,
        "local": len(local_lines),
        "local_lines": local_lines
    }

def print_result(res):
    """简洁格式化输出单篇结果"""
    if not res:
        return
    
    if res["total"] == 0:
        print(f"📄 {res['file_name']:<30} ⚪ 无图片")
        return

    if res["local"] == 0:
        print(f"📄 {res['file_name']:<30} ✅ 全部已上图床 (共 {res['total']} 张)")
    else:
        line_info = ", ".join(map(str, res['local_lines'][:8]))
        if len(res['local_lines']) > 8:
            line_info += f", ...等共{len(res['local_lines'])}处"
        print(f"📄 {res['file_name']:<30} ⚠️  有 {res['local']} 张本地图片未上传 (行号: {line_info})")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    blog_root = os.path.abspath(os.path.join(script_dir, ".."))
    posts_dir = os.path.join(blog_root, "content", "posts")

    # 1. 如果用户传入了具体文件或文件夹路径
    if len(sys.argv) >= 2:
        target = sys.argv[1]
        if not os.path.isabs(target):
            target = os.path.join(os.getcwd(), target)

        if os.path.isfile(target):
            res = scan_markdown_file(target)
            print("=" * 60)
            print_result(res)
            print("=" * 60)
            return
        elif os.path.isdir(target):
            scan_dir = target
        else:
            print(f"❌ 路径不存在: {target}")
            return
    else:
        # 2. 默认扫描整站所有文章目录 content/posts
        scan_dir = posts_dir

    if not os.path.exists(scan_dir):
        print(f"❌ 找不到文章目录: {scan_dir}")
        return

    md_files = []
    for root, _, files in os.walk(scan_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))

    print("=" * 65)
    print(f" 🔍 正在扫描博客文章图片上传状态 (共发现 {len(md_files)} 篇文章)")
    print("=" * 65)

    total_unuploaded = 0
    files_with_issues = 0

    for f_path in md_files:
        res = scan_markdown_file(f_path)
        if res:
            print_result(res)
            if res["local"] > 0:
                total_unuploaded += res["local"]
                files_with_issues += 1

    print("-" * 65)
    if total_unuploaded == 0:
        print(" 🎉 检查完毕：所有文章的图片均已成功上传至图床，无遗留本地图片！")
    else:
        print(f" ⚠️  检查完毕：共有 {files_with_issues} 篇文章存在未上传图片，合计 {total_unuploaded} 张本地图片需要上传。")
    print("=" * 65)

if __name__ == '__main__':
    main()
