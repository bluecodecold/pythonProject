import os
from add_data import add_data
from delete_data import delete_data
from search_data import search_data
from modify_data import modify_data
from statistics_data import statistics_data
from sort_data import sort_data

# 初始化数据文件夹
if not os.path.exists("datasss"):
    os.mkdir("datasss")
os.chdir("datasss")

media_types = ['movie', 'book', 'series', 'music']

def main():
    print("欢迎来到 '豆瓣酱' 管理系统!")
    while True:
        print("\n请选择操作：")
        print("1. 增  2. 删  3. 查  4. 改  5. 统计  6. 排序  0. 退出")
        select = input("输入数字选择：").strip()
        if select == '1':
            add_data(media_types)
        elif select == '2':
            delete_data(media_types)
        elif select == '3':
            search_data(media_types)
        elif select == '4':
            modify_data(media_types)
        elif select == '5':
            statistics_data(media_types)
        elif select == '6':
            sort_data(media_types)
        elif select == '0':
            print("退出系统，拜拜！")
            break
        else:
            print("无效选择，请重新输入！")

if __name__ == "__main__":
    main()
