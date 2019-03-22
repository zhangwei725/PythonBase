"""
1. 员工信息
   {
       'no':1,
       'name':'李大锤',
       'join_date':'2019-01-11',
       'phone':'110',
       'sal':10000000.00,
       'job':'it',
   }

2. 添加员工信息
    要求手机号必须唯一
    工号自增  第一个员工工号 1
3. 删除员工信息
   - 可以通过名字(name) 或者编号(no) 或者 手机号(phone)
4. 查询员工信息
   - 查询方式有三种 可以通过员工姓名模糊查询 例如可以输入李  字符串方法
   - 可以通过手机号(phone)来查询
   - 还可以通过职位(job查询)
5. 更新员工信息
   - 根据编号更新工资
   - 通过职位来更新工资
"""
emp_list = []
no = 1


# 快捷键  shift +  F6  全局修改名字

def add_emp(phone, name, job):
    global no
    """
    添加员工信息
    :param phone:
    :param name:
    :param job:
    :param no:
    :return: emp   如果 emp是一个空字典表示添加失败  否则就是添加成功
    """
    emp = {}
    if emp_list:
        # 表示已经有注册的员工, 判断手机是否已经存在
        for temp_emp in emp_list:
            if phone in temp_emp.values():
                print('手机号已存在')
                break
            else:
                # 表示手机号不存在 可以正常的添加
                emp.update(name=name, phone=phone, job=job, no=no)
                emp_list.append(emp)
                no += 1
    else:
        emp.update(name=name, phone=phone, job=job, no=no)
        emp_list.append(emp)
        no += 1
    return emp


def del_emp(name):
    is_del = False
    """
    删除员工
    :param name:通过手机号,姓名或者工号
    :return: True 表示删除成功, False表示删除失败
    """
    for emp in emp_list:
        if name in emp.values() or name == str(emp.get('no')):
            is_del = True
            emp_list.remove(emp)
            break
    return is_del


def find_emp(name, flag):
    """
    通过手机号,职位,姓名查询
    :param name:
    :param  flag 1 表示姓名查询  2 表示手机号查询
    :return:
    """
    emps = []
    if flag == 1:

        # 通过姓名查询
        for emp in emp_list:
            temp = emp.get('name')
            #  字符串方法
            if temp.find(name) != -1:
                emps.append(emp)

    elif flag == 2:
        for emp in emp_list:
            if name in emp.values():
                emps.append(emp)
    else:
        print('你可真秀')
    return emps


def update_emp():
    pass
