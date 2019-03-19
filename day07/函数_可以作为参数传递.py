# 函数如果想作为参数传递直接写函数名  不要使用函数名()

def test():
    print('测试代码')


def show(func):
    print("这个是show方法执行")
    func()

show(test)
