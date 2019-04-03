# li = [i for i in range(100000000000)]


# 当我们一次性加载大量数据的时候,就有可能造成内存紧张
# 大文件   10G    500M

# yield

def gener():
    print('第一个')
    yield 1
    print('第二歩')
    yield 2


if __name__ == '__main__':
    g = gener()
    print(next(g))
    print(next(g))
