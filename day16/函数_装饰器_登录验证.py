"""
登录验证
如果通过验证了,直接跳转过购物车
否则就提示请用户登录
"""

is_login = False


def login(username, password):
    global is_login
    is_login = True if username == 'admin' and password == '123456' else False
    return is_login


def auth(username, password):
    def wrapper(func):
        # args  元组   **kwargs
        def inner(*args, **kwargs):
            if is_login:
                result = func(*args, **kwargs)
                return result
            else:
                uname = input('请输入用户名!!!')
                pwd = input('请输入密码')
                login(username=uname, password=pwd)

        return inner

    return wrapper


@auth(username='admin', password='123456')
def index():
    print("欢迎{}来到xxx论坛首页!!!")


@auth(username='admin', password='123456')
def shop_car():
    print('娃娃')
    print('手机')
    print('生活用品')


if __name__ == '__main__':
    index()
    shop_car()
