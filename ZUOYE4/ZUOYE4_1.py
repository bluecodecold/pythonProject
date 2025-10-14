my_string = input("请输入一段字符串:")
print(f"第一个字符串为: {my_string[0]}")

print(f"最后一个字符串为: {my_string[-1]}")

if len(my_string) % 2 != 0:
    print(f"若字符数为奇数，则中间的字符为: {my_string[len(my_string)//2]}")

print(f"倒数三个字符为: {my_string[-3::]}")

print(f"倒序打印字符串为: {my_string[::-1]}")
