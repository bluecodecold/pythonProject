import json
import os

def statistics_data(media_types):
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

    total_score = sum(d["score"] for d in data)
    count = len(data)
    avg = total_score / count
    print(f"{media_type} 总记录数: {count} 平均评分: {avg:.2f}")
