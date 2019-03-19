# 列表
# 在控台给出提示信息如下
# 名字管理练习：1901班所有的学生姓名
#     1.查找学生姓名
#     1.1 > 如果学生信息存在则输出该学生姓名
#     1.2    否则查无此人
#     2.增加学生姓名
#     2.2> 如果学生姓名存在在提示,该学生信息已经存 重新输入
#     2.3>  提示添加成功
#     3.修改学生姓名
#     3.1 通过索引修改  提示输入索引  输入姓名
#     3.2 否则提示修改失败
#     4.删除学生
#     4.1 提示输入姓名  删除学生
#     5.退出系统
#     break

students = ['菲菲']
while True:
    print('=========欢迎来到1901学生姓名简易管理系统============')
    print('1.查找学生姓名')
    print('2.增加学生姓名')
    print('3.修改学生姓名')
    print('4.删除学生')
    print('5.退出系统')
    print('=====================================================')
    no = int(input('请选择相关的操作:\n'))
    if no == 1:
        # 查询学生
        name = input('请输入要查询学生的姓名')
        if name in students:
            print(name)
        else:
            print('查无此人')
    elif no == 2:
        # 增加学生姓名
        # append(obj)  insert(index,obj)
        name = input('请输入要添加学生的姓名:\n')
        if name:
            # 判断输入的学生的姓名是否已存在
            if name in students:  # 如果存在返回True
                print('该学生已存在!!!,请重新输入')
            else:
                # 将该学生姓名添加到系统中
                students.append(name)
                print('添加成功')
        else:
            print('输入的姓名有误,请重新输入!!!')
    elif no == 3:
        # 修改学生姓名 输入索引号   输入新的姓名
        #      列表  修改 只能通过 列表[索引] = 值的方式修改
        idx = int(input('请输入学生编号(索引号)'))
        # 判断编号必须在合理的范围内   大于0 小于长度
        if 0 <= idx < len(students):
            name = input('请输入学生姓名!!!')
            students[idx] = name
            print('修改成功')
        else:
            print('你输入的学生编号不存在!!!')
    elif no == 4:
        # 4.删除学生
        # pop(index) remove(元素的值)
        name = input('请输入学生的姓名:\n')
        students.remove(name)
        print('删除成功')
    elif no == 5:
        # 5.退出系统
        print('欢迎下次光临!!!')
        break
    else:
        print('智商不足.请充值!!!')
    print('条件语句结束!!!!!! 进入下一次循环')
