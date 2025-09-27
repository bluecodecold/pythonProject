NUMBER = int(input("请输入三位整数"))
number_one = NUMBER // 100
number_two = NUMBER // 10 % 10
number_three = NUMBER % 100 % 10
print(f"倒序为{number_three}{number_two}{number_one}")
