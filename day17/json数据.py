"""
进行数据传输
JSON
"""
# 字典
# 列表嵌套字典

"""
json        python
string       str
数字类型     int   float
false        False
true         True
null         None
array        list
object       字典

注意事项:  python 目前不支持自定义对象进行json转化


"""

# json_data = "{'key':value,'key':value}"
#
# json_data = "[{'key':value,'key':value},{'key':value,'key':value}]"

"""
序列化  
反序列化
"""

# 序列化
# 将python数据转化成json字符串

"""
将字典转化成json字符串
"""

import json

"""
序列化
"""


def serialize_dict():
    # 将字典转化成json数据
    user = {'name': '小明', 'age': 20, 'price': 1.00, 'sex': True, 'money': None}
    json_data = json.dumps(user)
    return json_data


"""
反序列化
"""


def deserialztion_dict(json_data):
    # 将json数据转化成python中的数据格式
    users = json.loads(json_data)
    print(type(users))
    name = users.get('name')
    print(name)
    print(users)


def serialize_list():
    users = [{'name': '小明', 'age': 20, 'price': 1.00, 'sex': True, 'money': None},
             {'name': '小明', 'age': 20, 'price': 1.00, 'sex': True, 'money': None}]
    data = json.dumps(users)
    print(type(data))
    print(data)
    return data


def deserialize_list(data):
    users = json.loads(data)
    print(type(users))
    print(users)
    return users


"""
字典嵌套列表
"""


def deserialize_dic():
    users = [{'name': '小明', 'age': 20, 'price': 1.00, 'sex': True, 'money': None},
             {'name': '小明', 'age': 20, 'price': 1.00, 'sex': True, 'money': None}]
    data = {
        'msg': 'hehe',
        'a': {
            'a': 'b',
            'b': users
        },
        'users': users
    }
    json_str = json.dumps(data)
    print(json_str)


class A:
    def __init__(self):
        self.a = '111'
        self.b = '2222'


#
if __name__ == '__main__':
    # serialize_dict()
    # data = serialize_list()
    # 反序列化
    # users = deserialize_list(data)
    # deserialize_dic()
    a_list = [A() for i in range(10)]
    json.dumps(a_list)
