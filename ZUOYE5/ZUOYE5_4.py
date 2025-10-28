def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("这三条边不能组成三角形")
    else:
        print("这三条边能组成三角形")



if __name__ == '__main__':
    a = int(input("请输入组成三角形的第一条边:"))
    b = int(input("请输入组成三角形的第二条边:"))
    c = int(input("请输入组成三角形的第三条边:"))

    triangle(a, b, c)
