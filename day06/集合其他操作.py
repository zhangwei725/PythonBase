# 添加操作
s = {1, 3, 4}
# s.add(2)
print(s)

# 更新操作  序列   字典注意是只会操作key
# s.update([1, 2, 4, 5, 6])
# s.update('123456')
# print(s)

s.update({'name': '小米', 1: '123'})

print(s)

# 随机删除元素
# ele = s.pop()
# 当元素的值不存在的时候 可以能报错
s.remove(1)
print(s)
# 存在则删除,不存在则不会做任何操作
s.discard(1)
