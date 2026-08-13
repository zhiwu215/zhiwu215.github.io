import os
import re
import requests

# ==================== 配置区 ====================
# 1. 你的 GitHub 图床仓库 (格式: 用户名/图床仓库名)
IMAGE_REPO = "zhiwu215/blog-img" 

# 2. 图片在图床仓库里的存储子目录 (例如 "posts" 或 "img")
#    如果在 PicGo 中未设置子目录，留空字符串 "" 即可
IMAGE_DIR = "" 

# 3. 博客文章所在目录
CONTENT_DIR = "content"
# ================================================

GITHUB_TOKEN = os.getenv("IMAGE_BED_TOKEN")
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_used_images():
    """遍历 content 目录下所有 .md 文件，提取出文章中引用的所有图片文件名"""
    used_images = set()
    # 正则匹配形如 filename.png / filename.jpg 等图片文件名
    pattern = re.compile(r'\/([^\/\s\)"\']+\.(?:png|jpg|jpeg|gif|webp|svg))', re.IGNORECASE)
    
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    matches = pattern.findall(content)
                    for match in matches:
                        used_images.add(match)
    print(f"✅ 在博客 Markdown 文章中共扫描到 {len(used_images)} 张在用图片。")
    return used_images

def get_remote_images():
    """通过 GitHub API 获取图床仓库目录下的所有图片文件"""
    path_suffix = f"/{IMAGE_DIR}" if IMAGE_DIR else ""
    url = f"https://api.github.com/repos/{IMAGE_REPO}/contents{path_suffix}"
    res = requests.get(url, headers=HEADERS)
    if res.status_code != 200:
        print(f"❌ 获取图床文件列表失败，HTTP 状态码: {res.status_code}")
        print(res.json())
        return []
    
    files = res.json()
    images = []
    for item in files:
        if item["type"] == "file":
            images.append({
                "name": item["name"],
                "path": item["path"],
                "sha": item["sha"]
            })
    print(f"📦 从 GitHub 图床仓库拉取到 {len(images)} 个图片文件。")
    return images

def delete_remote_image(file_info):
    """调用 API 删除图床仓库中的孤儿图片"""
    url = f"https://api.github.com/repos/{IMAGE_REPO}/contents/{file_info['path']}"
    data = {
        "message": f"chore: auto delete orphan image {file_info['name']}",
        "sha": file_info["sha"]
    }
    res = requests.delete(url, headers=HEADERS, json=data)
    if res.status_code == 200:
        print(f"🗑️ 成功删除孤儿图片: {file_info['name']}")
    else:
        print(f"❌ 删除失败: {file_info['name']}, 错误: {res.text}")

def main():
    if not GITHUB_TOKEN:
        print("❌ 未检测到 IMAGE_BED_TOKEN 环境变量，脚本退出。")
        return

    used_images = get_used_images()
    remote_images = get_remote_images()

    orphan_count = 0
    for img in remote_images:
        # 如果图床里的图片文件名没有在任何 Markdown 中引用过，即判定为孤儿图片
        if img["name"] not in used_images:
            print(f"🔍 发现孤儿图片: {img['name']}")
            delete_remote_image(img)
            orphan_count += 1

    print(f"🎉 清理完成！共删除 {orphan_count} 张孤儿图片。")

if __name__ == "__main__":
    main()
