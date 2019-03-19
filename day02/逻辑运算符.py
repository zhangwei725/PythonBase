# and 
# 
# 表达式  and  表达式  and  表达式 
# 1> 左边表达式如果返回的Flase,直接将表达式的值返回
# 2> 左边的表达式如果返回的True,返回右边表达式的值
# 

a = 10
b = 20
c = 30


print(a > c and b < c)
print(a < c  and b < c)

print(0 and 10)

print(10 and 1 + 10)


n1 = 10
n2 = 20


s1 = n1 and n2 

# 自动类型的转化
# 
#  '' ""  None  0   0.0 
#  现实中表示存在的东西就是True   不存在就是False
#  
# 输入
# st = input('请输入数字')
# st2 = input('请输入第二个数字')
# 输出
# a =  st and  st2

# print(a)

#   or的例子

a = 0
b = 1 
c = 3

d =  a > 0 > b  or  a < -1

print(d)


s1 = ''

s2 = '娇娇是个萌妹子'
d = not (s2  or s1)
print(d)


f = not  s1

print(f)











