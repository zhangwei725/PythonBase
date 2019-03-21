def login():
    print('登录方法')


li = [1, 2, 3]


def register(name, password, email):
    user = {}
    if name and password and email:
        user.update(name=name, password=password, email=email)
    else:
        print('格式不正确!!!')
    return user


# 导入包的时候记住 不要去导入__init__文件 而是直接导入包名就行了


print(home.name)
