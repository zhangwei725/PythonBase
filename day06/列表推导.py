# 快速创建列表
# 语法格式
# 列表 =[表达式  for 变量 in 列表]
# 列表 =[表达式  for 变量 in 列表 if 条件]
# nums = []
# for item in range(1, 101):
#     nums.append(item)
#
# print(nums)
# 等价于
nums = [item for item in range(1, 101)]
print(nums)

# 求100以内的偶数用列表添加
# li = []
# for item in range(1, 101):
#     if item % 2 == 0:
#         li.append(item)

li = [item for item in range(1, 101) if item % 2 == 0]

print(li)

#  求1-10以内所有数字的平方存入列表
li = [i ** 2 for i in range(1, 11)]
# 使用列表推导求1-100以内能被3整除的所有数

li = [item for item in range(1, 101) if item % 3 == 0]
print(li)