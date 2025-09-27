time = input("请输入总秒数")
hour = int(time) // 3600
minute = int(time) % 3600 // 60
second = int(time) % 60
print(f"{time}秒为{hour}时零{minute}分{second}秒")
