# 通过字典[key] = 值
# 当键存在的时候是做修改的操作
# 当键不存在的时候才是添加的操作

shop = {'name': '娃娃',
        'price': 368.00,
        'msg': '白天么么哒,晚上哈哈哈',
        }
# 添加商品上架的日期
shop['date'] = '2019-3-15'
print(shop)

# 内置方法
# 字典.setdefault(key,value)
# 参数 key是往字典中添加的key 必须不可变的一般是字符串
# 参数  value是字典添加的值

shop.setdefault('sex', '女')
# 如果键存在的时候 不会做任何操作
shop.setdefault('name', '冰冰')

print(shop)
