import json
import os

def search_data(media_types):
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

    keyword = input("请输入名称或部分关键字搜索: ").strip().lower()
    results = [d for d in data if keyword in d["name"].lower()]

    if not results:
        print("未找到记录！")
    else:
        print(f"\n找到 {len(results)} 条记录：")
        for d in results:
            print(f"\n名称: {d['name']}")
            print(f"日期: {d['date']}")
            print(f"评分: {d['score']}")
            print("简评:")
            for line in d['comment']:
                print("  ", line)
