import copy

"""

"""
li = [1, 3, 4, 5, {'a': 'b', 'c': 'd'}]

# 深拷贝
new_list = copy.deepcopy(li)

print(id(new_list[-1]))

print(id(li[-1]))

li[-1]['a'] = 'f'

print(new_list)
