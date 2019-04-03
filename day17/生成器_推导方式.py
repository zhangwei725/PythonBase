# 使用推导语法创建生成器
generator = (i for i in range(100000000000000))


# for i in generator:
#     print(i)


# 1 1 2 3  5  8  13
# 第一个数 + 第二个数 = 第三个
# 斐波拉契 使用生成器的方式实现斐波拉契数
#  爬虫  爬url地址
def fib(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, b + a


if __name__ == '__main__':
    for i in fib(100):
        print(i)
