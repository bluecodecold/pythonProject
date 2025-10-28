

def create(stu):
    print("请先创建学生信息(按*停止）")
    while True:

        name = input("请输入名称:")
        gender = input("请输入性别:")
        phone_number = input("请输入电话号:")
        if name == "*" or gender == "*" or phone_number == "*":
            break
        student = {'name': name, 'gender': gender, 'phone_number': phone_number}
        stu.append(student)



def add(stu):
    print("请输入添加的学生信息(输入*停止）:")
    while True:
        name = input("请输入名称:")
        gender = input("请输入性别:")
        phone_number = input("请输入电话号:")
        if name == "*" or gender == "*" or phone_number == "*":
            break
        student = {'name': name, 'gender': gender, 'phone_number': phone_number}
        stu.append(student)



def delete(stu):
    print("请输入要删除的学生信息:")
    num = int(input("想要删除第几位学生的信息"))
    delete_stu = stu.pop(num-1)
    print(f"被删除的学生信息为: {delete_stu}")


def modify(stu):
    print("请选择修改的学生信息:")
    num = int(input("想要修改第几位学生的信息"))
    print(f"该学生信息为: {stu[num-1]}")
    select = int(input("想要修改的信息为.1：姓名，2：性别，3：手机号"))
    if select == 1:
        name = input("请输入将要修改的姓名:")
        stu[num-1]["name"] = name
    elif select == 2:
        gender = input("请输入将要修改的性别:")
        stu[num-1]["gender"] = gender
    elif select == 3:
        phone_number = input("请输入将要修改的手机号:")
        stu[num-1]["phone_number"] = phone_number
    else:
        print("输入的选项有误！")

    return stu



def main():
    stu = list()
    create(stu)
    while True:
        print("欢迎来到学生管理系统,请选择你的功能:")
        print("*****************************")
        print("*****************************")
        print("******输入A：进行添加***********")
        print("******输入B：进行删除***********")
        print("******输入C：进行修改***********")
        print("******输入D：显示学生信息********")
        print("******输入E：进行退出***********")
        print("*****************************")
        print("*****************************")
        option = str(input(""))
        if option == "A":
            add(stu)
        elif option == "B":
            delete(stu)
        elif option == "C":
            modify(stu)
        elif option == "D":
            print(stu)
        elif option == "E":
           break


if __name__ == "__main__":
    main()