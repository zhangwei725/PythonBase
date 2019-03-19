
"""
bool

整形转化成布尔类型,所有0以外的数字转成True,只有0转化成False
浮点转成成布尔类型  除0.0以外所有的浮点型都转成True


"""

n1 = 10
n2 = -1
n3 = 0

print(bool(1000000))
print(bool(n3))


# 字符串转成-----布尔类型
# 除了 '' "" 空字符串转化成False  其他类型都转化True

s1 = ''
s2 = ""

s4 = " "


s3 = '爱是一道光'
print(bool(s1))
print(bool(s3))
print('空格字符串:',bool(s4))

n5 = None
print(bool(n5))
s3 = '-23.4'

print('s3 = ', float(s3))
"""
总结  其他类型转化成布尔类型 除了 0 0.0 '' ""  None
"""
cc = int(float("-123.45")) 
print(cc)

























