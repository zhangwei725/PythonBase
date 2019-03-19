# 序列操作  顾头不顾尾
s = 'you can you up no can no bb'
# 获取序列中的元素
# 通过索引获取序列中的元素
# print(s[0])
# print('从末尾开始取:{}'.format(s[-1]))
# print('从末尾开始取:{}'.format(s[-1]))
print(s[-100])
# 切片操作  截取序列某一部分的元素
# 语法格式
#  序列[start:end:step]
#  start 表示 开始的切的索引 默认0开始
#  end   表示 结束切的索引  默认取末尾
#  step  步长  默认1   注意事项  不能为0  可正可负  负数表示从右边开始切
#    0123456789
s = 'you can you up no can no bb'
# 只写一个参数表示起始索引 截取到末尾
# print(s[3:])
# 从末尾开始截取
# print(s[-2:])
# 注意  截取结束的索引要比开始的要大(步长为正数)
# print(s[:10])
# 开始截取的索引默认是0  结束索引为负
# print(s[:-10])
# 开始跟结束不使用默认值
# print(s[1:10])
#
# print(s[::2])

# '12345'
# 135  步长2
# 14  步长3
# print(s[1:10:3])
# 反转元素
print(s[::-1])
# 如果步长为负数 则开始的位置要比结尾的要大,否则截取的就是空
print(s[2:1:-1])

s = '0123456'

print(s[0:2])

# +
# *

# 是否包含
# in  是关键字  and    or
# 值  in  序列
#  值是否在这个序列中 如果值包含在序列中则返回True 否则返回False

s = '0123456'

print('0' in s)

# 实现原理
# i = "0"
# b = False
# for item in s:
#     if i == item:
#         b = True
#         break

# print(b)


# 判断序列的长度
# while   必须有终止条件
# 获取序列中所有的元素
s = '0123456'
i = 0

print(len(s))
while i < len(s):
    print(s[i])
    i += 1
# 123456去整形

s = '123456abc '
# max_num = ''
# for item in s:
#     max_num = item if item > max_num else max_num
#
# print('最大的元素{}'.format(max_num))

print(max(s))


# for item in s:
#     print("for%s" % item)
