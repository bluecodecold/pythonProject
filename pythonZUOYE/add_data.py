import json
import os


def add_data(media_types):
    print("请选择媒体类型：", media_types)
    media_type = input("输入类型: ").strip().lower()
    if media_type not in media_types:
        print("类型错误！")
        return

    filename = f"{media_type}.txt"
    if not os.path.exists(filename):
        data = []
    else:
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except:
                data = []

    name = input("请输入名称: ").strip()
    year = input("年份: ").strip()
    month = input("月份: ").strip()
    day = input("日期: ").strip()
    score = input("评分(0-10): ").strip()
    print("请输入简评（输入'我说完了'结束）：")
    lines = []
    while True:
        text = input()
        if text.strip() == "我说完了":
            break
        lines.append(text)

    record = {
        "name": name,
        "date": f"{year}-{month}-{day}",
        "score": float(score),
        "comment": lines
    }
    data.append(record)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"{name} 已添加到 {filename}！")
