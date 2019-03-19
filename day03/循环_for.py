# 
# 作用 通常用于遍历 列表 字符串  字典   可迭代
# 

s = 'hello12312321321'


# 第一步 底层先去循环获取字符串的长度获取里面的元素
# 第二歩 将元素赋值给定义的变量
# 第三歩 执行循环题的代码
# 第四步 循环体执行完成之后
# 执行第一步的操作

# for  item  in  s:
# 	print(item)


# 1 -5
# s = '12345'
# for x in s:
# 	print(x)
	
# 
# 顾头不顾尾  
# python 提供range 

# range([start],end,[step])
# 参数说明
#  start  计数开始的数,默认0  range(5) 等价于 range(0,5)
#  end    计数结束的数,不包含5
#  step

# nums  = range(1, 5)

# nums = range(5)

# 步长

nums = range(1, 10)   #1 3 5 7 9

for num in nums:
	print(num)
# 输出1-100以内的所有的偶数
# ! 

for i  in range(1, 101):
	if not i % 2:
		print('偶数:{}'.format(i))





i = 1
while  i <= 100 :
	if  i % 2 == 0:
		print('偶数:{}'.format(i))
	i + =1		











