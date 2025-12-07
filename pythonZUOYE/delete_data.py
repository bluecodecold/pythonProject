import json
import os


def delete_data(media_types):
    print("请选择媒体类型：", media_types)
    media_type = input("输入类型: ").strip().lower()
    if media_type not in media_types:
        print("类型错误！")
        return

    filename = f"{media_type}.txt"
    if not os.path.exists(filename):
        print("没有该媒体类型的数据！")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    name = input("请输入要删除的名称: ").strip()
    new_data = [d for d in data if d["name"] != name]

    if len(new_data) == len(data):
        print("未找到该记录！")
    else:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)
        print(f"{name} 已删除！")
