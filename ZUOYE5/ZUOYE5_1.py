def compare(a, b, c):
    max_number = a
    if max_number < b:
        max_number = b
    if max_number < c:
        max_number = c

    return max_number


if __name__ == '__main__':
    a = int(input("请输入第一位整数: "))
    b = int(input("请输入第二位整数: "))
    c = int(input("请输入第三位整数: "))

    max_number = compare(a, b, c)
    print(f"三位数中最大的数字为{max_number}")
