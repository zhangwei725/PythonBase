"""
第一个数据校验
#  计算

属性

"""

"""
简洁

"""


class Shop:

    def __init__(self, no, name, discount_price):
        self.no = no
        self.name = name
        # 对数据校验
        self._price = 0
        self.discount_price = discount_price

    # def get_price(self):
    #     return self._price

    # 获取值的操作

    # def set_price(self, value):
    #     if value > 0:
    #         self._price = value
    #     else:
    #         raise Exception('输入的价格不符合规范!!!')

    # 等价于 get_price
    @property
    def price(self):
        return self._price

    # 赋值操作
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise Exception('输入的价格不符合规范!!!')


"""
作用
如何操作
1> 声明方法  在方法上面使用@property装饰器 注意方法一定要有返回值
2> 赋值操作  使用方法名(self,传入的值),在方法上面使用第一步声明的方法名.setter

如何使用
通过对.属性








"""
if __name__ == '__main__':
    phone = Shop(no=1, name='手机', discount_price=100)
    # phone.price  =  -1000
    phone.set_price(1000)
    print(phone.get_price())
