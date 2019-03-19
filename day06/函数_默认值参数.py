# 默认值参数  声明参数名=默认值,
# 当我们传递了参数直接使用传递至,否则就是用默认值
# 参数可以可不传

"""
phones = [{'name':'华为','price':8000,00,version:1}]
使用函数的方式去实现
手机管理系统

1/添加手机
2> 根据手机名删除手机
3> 根据手机名更新价格
4> 查询库存(获取所有的手机信息)
5> 退出系统
"""


def login(username, password, is_remember=True):
    """
    登录功能
    :param username: 用户名
    :param password: 密码
    :return:  True  表示登录成功 False 表示登录失败
    """
    print(is_remember)
    if username == 'admin' and password == '123':
        if is_remember:
            print('保存账号密码')

        return True
    else:
        return False


login('admin', '123', True)
