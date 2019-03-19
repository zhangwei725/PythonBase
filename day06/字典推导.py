#  字典 = { key:value for key ,value in 可迭代对象}
#  字典 = { key:value for key ,value in 可迭代对象  if  条件表达式}

shop = {'Title': '手机', 'Price': 8000.00}
temp = {}
# for key, value in shop.items():
#     # 字符串的常用方法  将所有的字母转化成小写
#     lower_key = key.lower()
#     #   不能使用update方法
#     temp[lower_key] = value
#
# print(temp)

for key in shop.keys():
    # 'title' =   shop.get("Title")
    temp[key.lower()] = shop.get(key)

# temp = {key.lower(): shop.get(key) for key in shop.keys()}

# 想把列表转化字典
# 0,元素 1.元素 enumerate(列表)
# 列表的索引作为key  列表元素作为值

li = ["a", 'b', 'c', 'd']
# temp = {}
# for key, value in enumerate(li):
#     temp[key] = value
# print(temp)

temp = {key: value for key, value in enumerate(li)}

print(temp)

# 只存储索引大于1的元素


# temp = {}
# for key, value in enumerate(li):
#     if key > 1:
#         temp[key] = value
# print(temp)
#
temp = {key: value for key, value in enumerate(li) if key > 1}
print(temp)
