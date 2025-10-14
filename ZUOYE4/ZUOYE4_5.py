my_list = []

while True:
    num = input("请输入添加进入列表的值,按n停止: ")
    if num == "n":
        break
    my_list.append(int(num))
print(f"列表为: {my_list}")
max_number = my_list[0]
for i in my_list:
    if i > max_number:
        max_number = i
print(f"最大值为{max_number}")


