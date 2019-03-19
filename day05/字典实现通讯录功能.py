# 1、实现通讯录功能(字典的方式)
# 1. 查询联系人
# 2. 添加联系人
# 3. 更新联系人
# 4. 删除联系人
# 5. 退出程序
# 用来存储联系人的通信相关的信息
contacts = {'宝宝': 110}

while True:
    print('=======简易通讯录======')
    print('1. 查询联系人')
    print('2. 添加联系人')
    print('3. 更新联系人')
    print('4. 删除联系人')
    print('5. 退出程序')
    print('=======================')
    num = input('请选择相关的操作!!!')
    if num == '1':
        # 查询的操作
        name = input('请输入联系人姓名:\n')
        if name:
            #  查询  get()  字典[key]  for循环
            #
            #  如果in跟字典配合使用 判断键是否存在
            if name in contacts:
                print('{} : {}'.format(name, contacts.get(name)))
        else:
            print("输入的用户名不能为空!!!")

    elif num == '2':
        # 添加操作
        name = input('请输入联系人姓名:\n')
        if name in contacts:
            print('联系人已存在!!!! 请重新选择!!!')
        else:
            phone = input('请输入电话号码!!!')
            #          字典[key] = 值   update(k=v)  setdefault(k,v)
            contacts[name] = phone
    elif num == '3':
        #  更新操作
        #  update()  字典[key] = 值
        name = input('请输入联系人姓名:\n')
        if name in contacts:
            phone = input('请输入电话号码!!!')
            contacts[name] = phone
        else:
            print('联系人不存在')
    elif num == '4':
        # pop
        name = input('请输入要删除的联系人的姓名:\n')
        if name in contacts:
            contacts.pop(name)
            print('删除成功!!!')
        else:
            print('联系人不存在!!!')
    elif num == '5':
        print('系统安全退出ing')
        break
    else:
        print('输入有误请重新输入')

    print('本次循环结束,继续下一次循环')

# 字符串的常用操作
# 推导
# 集合  去重
