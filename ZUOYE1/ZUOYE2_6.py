year = input("请输入一个年份")
year = int(year)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("true")
else:
    print("false")
