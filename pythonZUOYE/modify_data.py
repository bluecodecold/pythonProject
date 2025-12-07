import json
import os

def modify_data(media_types):
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

    name = input("请输入要修改的名称: ").strip()
    found = False
    for d in data:
        if d["name"] == name:
            found = True
            print("当前记录：", d)
            score = input("新评分(Enter跳过): ").strip()
            if score:
                d["score"] = float(score)
            print("请输入新简评（输入'我说完了'结束，Enter跳过）:")
            lines = []
            while True:
                text = input()
                if text.strip() == "我说完了":
                    break
                elif text.strip() == "" and not lines:
                    break
                lines.append(text)
            if lines:
                d["comment"] = lines
            break
    if found:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"{name} 已修改！")
    else:
        print("未找到该记录！")
