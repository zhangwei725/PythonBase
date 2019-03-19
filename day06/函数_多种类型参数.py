# 如果函数声明的参数里有种不同类型的参数
# 声明声明必要参数必须放在最左边,其次是默认值参数,再次可变长度参数,最后是可变长度关键字参数

def fun(a, b, default=0, *args, **kwargs):
    print(a)
    print(b)
    print(default)
    print(args)
    print(kwargs)


fun(1, b=1, default=12, n=10)
