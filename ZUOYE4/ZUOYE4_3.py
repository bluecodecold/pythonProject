my_string = input("请输入一段字符串: ")
if my_string[::-1] == my_string:
    print(f"{my_string}是回文！")

else:
    print(f"{my_string}不是回文！")