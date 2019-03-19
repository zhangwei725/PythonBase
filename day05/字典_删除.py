# 删除操作 字典.pop(key)
#  字典.pop

shop = {'name': '娃娃',
        'price': 368.00,
        'msg': '白天么么哒,晚上哈哈哈',
        'k': '1',
        '宝宝': '这个是一个值',
        'baby': '左勇杰',
        }
# 说明
#  通过键删除字典中的元素
#  参数1 键  当键不存在的时候,直接报错


value = shop.pop('baby')
print(value)
print(shop)

# 当前不存在的情况 报错KeyError:
# shop.pop(1)
"""
随机删除字典中的元素  返回被删除的元素
"""
item = shop.popitem()
print(item)
# 清空字典
shop.clear()
print(shop)

new_shop = shop.copy()


