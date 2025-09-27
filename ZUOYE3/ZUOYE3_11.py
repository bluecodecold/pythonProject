import random
score = 0
for i in range(0, 11):
    number_one = random.randint(1, 10)
    number_two = random.randint(1, 10)
    answer = int(input(f" {number_one} + {number_two} 的答案为: "))
    if answer == number_one + number_two:
        score += 5
        print("答对！")
    else:
        score -= 5
        print("答错！")
print(f"你的总分为{score}!")
