# key:value这种形式的数据类型就叫映射类型
# 但是python不保证你的数据是按着你声明的顺序

user = {'name': '娇娇',
        'height': 14.0,
        'active': True,
        'address': [1, 2, 3, 4],
        'age': 19,
        1: '',
        }

# 第一种方式  通过  字典[kye]的方式获取
d1 = user['name']
print(d1)
# 当key不存在的时候报错
# print(user[10])

#  第二种方式   字典,get(key)
# 通过key获取值 当key不存在的时候返回一个默认值None
#

age = user.get('age')
print(age)
# 当key不存在的时候返回默认值
# 否则就返回获取到的值
value = user.get(10, '这个是我设置的默认值')

print(value)

# 获取字典中所有的key
keys = user.keys()
for key in keys:
    print(key)
# 遍历所有的值
# 字典.values()
values = user.values()
for value in values:
    print(value)

# 同时获取键值对
# 字典.items()

items = user.items()
print(type(items))

for key, value in items:
    print(key, value)








