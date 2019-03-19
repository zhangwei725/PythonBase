# 1> 如何声明   [] -> False
# 声明空列表
li1 = []
#  声明有元素的列表
li2 = [1, 2]
# 声明包含多种类型的列表
li = [1, '娇娇', '空空', '宝宝', True]
# 如何操作
"""
1> 通过索引获取元素
"""
item = li[0]
print(item)

# bug
# 注意 当索引大于长度-1的时候 IndexError: list index out of range
# item1 = li[100]
item2 = li[-1]

print(item2)








