My_list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("正序相隔两个为: ")
for i in My_list[0::2]:
    print(i)
print("倒序相隔两个为: ")
for i in My_list[::-2]:
    print(i)


