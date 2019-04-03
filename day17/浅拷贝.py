import copy

# 基本类型不可变  字符串不可变  元组不可变
#  字典  列表  集合
# 浅拷贝,当对象里的可变类型的数据发生改变时候,
# 所有浅拷贝的对象的可变类型的数据也会发生改变

li = [1, 2, 3, 4, [1, 3, 4]]

# 浅拷贝

new_list = li.copy()
new_list1 = li.copy()
new_list2 = li.copy()
new_list2[-1][0] = 10
print(new_list)
print(new_list1)
print(new_list2)
# 调用copy.copy来浅拷贝对象
li1 = copy.copy(li)


