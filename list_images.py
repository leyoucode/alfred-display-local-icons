import os
import json
import sys

# 指定图片文件夹路径
FILE_FOLDER = os.getenv("FILE_FOLDER", "./")

# 从环境变量中获取支持的图片扩展名，并解析为集合
IMAGE_EXTENSIONS = set(os.getenv("IMAGE_EXTENSIONS", ".jpg,.jpeg,.png,.gif,.bmp").split(','))


def list_images(folder, filter_text):
    """列出指定文件夹及其子文件夹中的所有图片文件，并根据过滤文本进行过滤"""
    images = []
    for root, _, files in os.walk(folder):
        for file in files:
            if os.path.splitext(file)[1].lower() in IMAGE_EXTENSIONS and filter_text.lower() in file.lower():
                images.append(os.path.join(root, file))
    return images

def main(filter_text):
    images = list_images(FILE_FOLDER, filter_text)
    items = []
    for image in images:
        items.append({
            "title": os.path.basename(image),
            "subtitle": image,
            "arg": image,
            "type": "file",
            "icon": {
                "path": image
            }
        })
    
    # 输出结果给 Alfred
    print(json.dumps({"items": items}))

if __name__ == "__main__":
    # 获取用户输入的过滤参数
    filter_text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else ""
    main(filter_text)

