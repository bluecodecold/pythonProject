import random
number = (random.randint(1, 1000))
signal = True
while signal:
    guess_number = int(input("请随便猜测一个数"))
    if guess_number > number:
        print("猜大了！")
    elif guess_number < number:
        print("猜小了！")
    elif guess_number == number:
        print("猜对了！")
        print(f"正确数字是{number}!")
        signal = False

