print("水仙花数目为:")
for number in range(100, 1000):
    number_one = number // 100
    number_two = number // 10 % 10
    number_three = number %10
    if number == number_one**3 + number_two**3 + number_three**3:
        print(f"{number}")
        continue