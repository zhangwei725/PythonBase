# 不可变的数据类型有哪些  数字类型,布尔类型   字符串   元组
# 声明空的元组
tup = (1, 2, 3, '111', True)
print(type(tup))

# 注意 当元组的里元素只有一个的时候 一定要加上,
tup1 = ('11111',)
print(type(tup1))
# 基本操作
# 不能在原有的元组上面进行增删改的操作
"""
1> 通过索引查询元组中元素
2> 
"""

names = ('宝宝', '杰杰', '凡凡', '盛盛', '菲菲')
print(names[0])
print(id(names))
"""
通过 for 循环
"""
for item in names:
    print(item)

"""
while循环

"""
"""
切片操作
"""
# 元组 + 元组
names1 = ('薇薇',)

# names = names1 + names

names += names1
print(names1)
print(names)

print(id(names))

# print(tup)

# 错误的方式
# names[1] = '1111111'
# print(names)

s = '1234'
s[0] = '哈哈'





