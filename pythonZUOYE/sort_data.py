import json
import os

def sort_data(media_types):
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

    if not data:
        print("没有记录！")
        return

    print("1. 按评分排序  2. 按日期排序")
    choice = input("选择排序方式: ").strip()
    if choice == '1':
        data.sort(key=lambda x: x["score"], reverse=True)
    elif choice == '2':
        data.sort(key=lambda x: x["date"], reverse=True)
    else:
        print("无效选择！")
        return

    print(f"\n{media_type} 排序结果：")
    for d in data:
        print(f"名称: {d['name']}, 日期: {d['date']}, 评分: {d['score']}")
