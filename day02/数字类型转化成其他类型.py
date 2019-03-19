#  整行 ----> 转化成其他类型
#  1> 字符串---->整形
#  1.2> 注意 非数字字符串不能转化成整形
#  
#  数字字符串  非数字
s1 = '123'
s2 = '宝宝'

n = int(s1) 
# 判断变量的类型
print(type(n))

print(n)

# 不能转化非数字(必须是纯数字)的字符串 (错误)

# n1 = int(s2)
# print(n1)

"""
浮点型转化成int


"""
f = 3.1415
f1 = 100.68
n2 = int(f)
n3 = int(f1)

print(n2)
print(n3)


"""
其他类型转化成float

float

"""

k1 = '-1.10'

m = float(k1)

k2 = 10
m1 = float(k2)
# 布尔类型转化成浮点型 
m2 = float(True)   # 1.0
m3 = float(False)  #

print(m)
print(m1)
print(m2)

print(m3)


"""
总结

字符串--->int
浮点型 --->int 
布尔 ---> int

"""

































