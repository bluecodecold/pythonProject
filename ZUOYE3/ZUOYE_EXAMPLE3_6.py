print("欢迎使用ATM系统".center(20, '*'))

count = 0
for i in range(3):
    print("请输入用户名和密码: ")
    username = input('用户名: ')
    userpwd = input("密码: ")
    count +=1
    if username == 'admin':
        if userpwd == 'abc':
            print("登录成功！")
            break
        else:
            print("登录失败,密码错误！")
            print("你还有%s次机会"%(3-count))
    else:
        print("登陆失败，该用户不存在")
        print('你还有%s次机会'%(3-count))
else:
    print("抱歉，已吞卡，请联系管理员.")