# 嵌套
sql = "select *  from  user where  username='123'"

print(sql)

"""
去掉空格 制表符(大空格)
strip  去掉左右两边的空格   注意不能去掉字符串中间的空格
lstrip  去掉左边的空格 
rstrip   去掉右边的空格
"""
s1 = '\t    a b c   \t\t'
# left   right
print('去掉左右两边的空格+制表符{}'.format(s1.strip()))
print('去掉左边的空格+制表符{}'.format(s1.lstrip()))
print('去掉右边的空格+制表符{}'.format(s1.rstrip()))

"""
分割字符串
split(str='')  
参数  
    str 默认情况下使用空格 制表符  换行符
        按指定的字符串进行切割
    num  切割的次数    
返回值
    list    
"""

s4 = '自古多情空余恨,唯 有 套路的\t人\n心'
url = 'xxx/xxxx/xxx/small.mp4'
print(s4.split())

print('指定切割符{}'.format(url.split('/')))

"""
字符串的替换
replace (old,new,count)
参数 
 必要  要替换的字符
 必要  用于替换的字符
 
返回值
 是一个新的字符串 
"""

s5 = '1234656abc'
print(s5.replace('abc', 'a'))

"""
字符串查找
find(sub,start,end)

参数
 sub 要查找的字符串
 start 开始索引的位置 默认值0

返回值
    返回第一次出现的索引位置
    如果不存在则返回 -1
    
"""
# 学it技术
s6 = '12345678'

print(s6.find('12c'))

print(s6.find('6', 3))

print(s6.rfind('8', -1))

"""
判断字符串
startswith
endswith
参数 1
    指定判断的字符串
参数 2
    start
参数 3 
    结束的位置    

"""
s7 = '致命打基'
print(s7.startswith('致'))

print(s7.startswith('致命'))

print(s7.endswith('打基'))
print(s7.startswith('命', 1))

"""

"""
# 12年 utf8
s8 = 'no zuo no die'
print(s8.count(''))

"""

大小写转化
用户名: 
    
"""
s8 = 'ABC'

print(s8.upper())
print(s8.lower())
# join

s9 = 'abcd'
print('-'.join(s9))

s10 = 'python了解一下'
print(s10.encode())
s11 = b'python\xe4\xba\x86\xe8\xa7\xa3\xe4\xb8\x80\xe4\xb8\x8b'

print(s11.decode())
