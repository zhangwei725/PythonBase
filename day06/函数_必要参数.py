
def login(username, password):
    """
    登录功能
    :param username: 用户名
    :param password: 密码
    :return:  True  表示登录成功 False 表示登录失败
    """
    if username == 'admin' and password == '123':
        return True
    else:
        return False


# 关键字参数(调用函数的时候)
# 在调用函数时传递参数
# 使用声明的参数的名字=值 中间不要有空格


# is_login = login('admin', '123')
print(end='\n')

is_login = login(password='123', username='admin')

print(is_login)
