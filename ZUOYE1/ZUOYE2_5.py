number = input("请输入一个四位数")
number = int(number)
number_one = number //1000
number_two = number // 100 % 10
number_three = number //10 % 10
number_four = number % 10
total = number_one + number_two +number_three+ number_four
print(f"四位数相加为{total}")
