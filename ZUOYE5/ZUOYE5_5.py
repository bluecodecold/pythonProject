def gongbeishu(num1, num2):
    total = num1 * num2
    chushu = gongyueshu(num1, num2)
    result = total // chushu
    print(f"最小公倍数为{result}")


def gongyueshu(num1, num2):
    yushu = num1 % num2
    chushu = num2
    while yushu != 0:
        beichushu = chushu
        chushu = yushu
        yushu = beichushu % chushu
    return chushu


if __name__ == "__main__":
    num1 = int(input("请输入第一位数： "))
    num2 = int(input("请输入第二位数： "))
    gongbeishu(num1, num2)
    