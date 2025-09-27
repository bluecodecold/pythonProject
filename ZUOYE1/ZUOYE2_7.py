number1 = input("请输入第一个数")
number2 = input("请输入第二个数")
number3 = input("请输入第三个数")
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)
max_number = number1
if number2 > number1:
    max_number = number2
    if number3 > max_number:
        max_number = number3
print(f"最大数为{max_number}")