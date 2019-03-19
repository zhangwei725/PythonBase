def func(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)


# 不能使用必要参数的方式
# func('admin', '123')
# 必须使用关键字参数
func(username='admin', password='123', a=10, b=30)

# *args   系统自动将多个参数封装元组
# **kwargs  系统会自动分装成字典  所以我们传递参数的时候也是键=值的方式去传递
