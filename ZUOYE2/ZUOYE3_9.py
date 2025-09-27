month = int(input("请输入一个月份"))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("该月份有31天")
elif month in [4, 6, 9, 11]:
    print("该月份有30天")

elif month not in range(1, 13):
    print("不存在该月份呢")

else:
    print("该月份有28或29天")
