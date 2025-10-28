def huiwen(num):
    re_num = 0
    num_original = num
    while num:
        re_num =re_num * 10 + num % 10
        num //= 10
    if re_num == num_original:
        print(f"{num_original}是回文数字")

    else:
        print(f"{num_original}不是回文数字")


if __name__ == '__main__':
    num=int(input("请输入你所想要检测的回文数: "))
    huiwen(num)