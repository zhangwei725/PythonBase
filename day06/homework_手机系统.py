"""
    phones = [{'name':'华为','price':8000,00,version:1}]
    使用函数的方式去实现
    手机管理系统
    1> 添加手机
    2> 根据手机名删除手机
    3> 根据手机名更新价格
    4> 查询库存(获取所有的手机信息)
    5> 退出系统
"""
# 持久化
# 复用代码


# 保存所有的手机信息
phones = [{'name': '小米', 'price': 8000.00, 'version': 1}, {'name': '华为', 'price': 8000.00, 'version': 1}]


# 不是功能

def add_phone(name, price, version):
    """
    #  添加手机信息
    :param name:  手机的名称
    :param price:  手机的价格
    :param version:  手机信号
    :return:
    """
    phone = {}
    phone.update(name=name, price=price, version=version)
    # 将手机添加到手机列中
    phones.append(phone)
    return True

"""
闭包  装饰器
"""
def del_phone_by_name(name):
    """
    通过手机名称删除手机
    :param name: 手机名
    :return: True 表示成功 False表示失败
    """
    """
    查找列中的每个字典的手机名,将该字典从列表中删除
    查询操作 
    删除的操作
    pop
    remove
    """
    # 遍历手机列表
    for phone in phones:
        # 判断手机名是否在字典中
        # if  name  == phone.get('name'):
        if name in phone.values():
            phones.remove(phone)
            break
    return True


def update_phone_price(name, price):
    """
    通过手机名更新手机价格
    :param name: 手机名
    :param price:  价格
    :return:
    """
    for phone in phones:
        if name in phone.values():
            phone.update(price=price)
            break
    #
    # phone = is_exist(name)
    # if phone:
    #     phone.update(price=price)
    return True


#  判断手机是否在手机列表中  手机
# def is_exist(name):
#     # 定义一个变量
#     temp = None
#     for phone in phones:
#         # exist = True if name in phone.values() else False
#         if name in phone.values():
#             temp = phone
#             break
#     return temp


while True:
    choose = int(input('请开始你的骚操作:\n'))
    if choose == 1:
        # 添加操作
        name = input('请输入手机的名字')
        price = input('请输入手机的价格')
        version = input('请输入手机的信号')
        is_add = add_phone(name, price, version)
        if is_add:
            print('添加成功')
        else:
            print('添加失败')

    elif choose == 2:
        # 删除操作
        print('===========删除开始===========')
        name = input('请输入要删除的手机名')
        is_del = del_phone_by_name(name)
        if is_del:
            print('删除成功')
    elif choose == 3:
        name = input('请输入手机名:')
        price = input('请输入手机价格:')
        is_update = update_phone_price(name, price)
    else:
        print('输入有误!!!请重新输入')

    print(phones)
