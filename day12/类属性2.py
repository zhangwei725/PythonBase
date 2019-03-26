"""
通过属性这种技术实现
本质对变量的赋值获取的操作

赋值的操作必须通过的数据校验
1. 声明获取方法,
2 在获取的方法上面加装饰器  @property
3 在方法中使用return 返回这个变量

"""
import hashlib

"""
可逆,AES DES
不可逆

对称加密
非对称加密

"""


class User:
    def __init__(self, username, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        self.username = username
        #  存密码不能明文
        self._password = None
        self._age = 1

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 1:
            self._age = age
        else:
            raise Exception('年龄不符合要求,请检查!!!')

    @property
    def full_name(self):
        return self.first_name + self.last_name

    def save(self, username, password):
        if username and password:
            md5 = hashlib.md5()
            md5.update(str.encode(password))
            print(md5.hexdigest())


#
class Shop:

    def __init__(self, no, name):
        self.no = no
        self.name = name
        # 对数据校验
        self._original_price = 0
        self._discount_price = 0
        # 获取折扣后价格

    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, original_price):
        if original_price > 0:
            self._original_price = original_price

    @property
    def discount_price(self):
        return self._discount_price

    @discount_price.setter
    def discount_price(self, discount_price):
        if discount_price > 0 and (discount_price <= self._original_price):
            self._discount_price = discount_price

    @property
    def price(self):
        return self._original_price - self.discount_price


"""
需要对数据进行处理(主要是这些数据一定要符合我们的业务逻辑)
对数据计算
# 

"""
if __name__ == '__main__':
    # user = User(username='123456', first_name='娇', last_name='余')
    # user.age = 10
    # print(user.age)
    # user.save(username=1111, password='2222')
    #
    # # print(user.first_name + user.last_name)
    # print(user.full_name)
    shop = Shop(no=1, name='手机')
    shop.original_price = 1000.0
    shop.discount_price = 2
    print(shop.price)
