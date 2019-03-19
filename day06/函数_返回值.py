#  使用return关键字
#  1> 没有返回值
#     1.1> 不写 return  不要使用变量去接受,直接调用函数就完事
#     1.2> 使用 return  后面不跟任何值
#     1.3> 使用return   None
#  2> 有返回值
#      2.1> 返回一个对象
#      2.2> 返回多个对象
# 元组
# break
# continue
def mut(n):
    if isinstance(n, int):
        return n - 10


# 传递三个数返回最小值跟最大值
def compare(a, b, c):
    """
     传递三个数返回最小值跟最大值
    :param a: 数字
    :param b: 数字
    :param c: 数字
    :return:   最大值跟最小值
    """
    max_value = max(a, b, c)
    min_value = min(a, b, c)
    return max_value, min_value


# 注意如果说我们用一个变量去接受多个返回值,系统将这个多个返回值封装元组
max_v, min_v = compare(1, 2, 3)

# 函数作用
# 参数  作用
# 返回值
# 注意事项
