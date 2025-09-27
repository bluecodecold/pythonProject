# import datetime
#
# year = int(input("请输入出生年份: "))
# month = int(input("请输入出生月份: "))
# day = int(input("请输入出生日期: "))
#
# today = datetime.date.today()
# next_birthday = datetime.date(today.year, month, day)
#
# if next_birthday < today:
#     next_birthday = datetime.date(today.year + 1, month, day)
#
# days_left = (next_birthday - today).days
# print(f"距离您下一个生日还有 {days_left} 天")

import datetime
year = int(input("请输入出生年"))
month = int(input("请输入出生月"))
day = int(input("请输入出生日"))
today = datetime.date.today()
next_birthday = datetime.date(today.year, month, day)
if next_birthday < today:
    next_birthday = datetime.date(today.year+1, month, day)
left_day = (next_birthday - today).days
print(f"距离下一次生日还有{left_day}天")
