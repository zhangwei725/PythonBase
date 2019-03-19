# 定义函数
print('1111')


#  for  in and  or while if   def
# def  函数名称(参数,参数,参数):
# 函数的语句块
# return  返回值

# a + b
# 无参无返回值

def show():
    print('这个是一个函数')


# 有参数无返回值
def add(num1, num2):
    print(num1 + num2)


def get(name):
    value = name * 100
    return value


get(10)

# 函数名()
# 可以给函数起别名
# show()

test = show

print(test)
#  show()

add(1, 2)




