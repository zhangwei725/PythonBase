# 可迭代对象
# 能够使用for循环遍历的都是可迭代对象

# 创建可迭代对象 iter()
# next()

# 特点
# 不能向后移动
# 也不能回到开始的位置

li = [1, 2, 3, 4]

it = iter(li)
# 将元组转化成迭代器对象
tup = (1,)
tup_iter = iter(tup)

dic = {'hello': 'world', '1': 222}
dic_iter = iter(dic)

s = {1, 2, 3, 4, 1}
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))

# for item in li:
    

