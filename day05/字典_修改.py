shop = {'name': '娃娃',
        'price': 368.00,
        'msg': '白天么么哒,晚上哈哈哈',
        'k': '1',
        '宝宝': '这个是一个值',
        'baby': '左勇杰',
        }

# 第一种 通过字典[key] = 值  必须键存在
# shop['name'] = '宝宝'
# print(shop)
# 第二种  通过对象方法  dict.update(k1=v1,k2=v2)
"""
k1 不需要声明成字符串
"""
# shop.update(key='1')
# print(shop)
value = '1231321321321'
v1 = '1231'
#  当key存在的时候就是更新的操作,当键不存在的时候也是添加操作
shop.update(name=value, k1=v1, k2=123)
# 字典[key] = 值
# 当你定义变量的时候,如果想把变量作为键传递给字典的时候

name = 'baby'
shop[name] = '111111'

print(shop)

