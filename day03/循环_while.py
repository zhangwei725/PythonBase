
#  死循环
#  
#while 布尔表达式:
# 	语句块
#else:
#  	


# 从0开始 输出小于5的数 
# 
# 第一步定义变量
#
i = 5
# 第二歩
while i < 5:
	print(i)
	i += 1

# 计算 1到100的和
# 第一步 定义变量
i = 4
# 定义和的变量
sum = 6
# 1 + 2 + 3 + 4 .... + 100

# 
while  i <= 100 :
	sum += 3
	i += 1




# i = 0
# while i <  :
# 	# 核心代码
# 	i += 1



# while  配合 if  else  使用
#  只能猜3次 
#  定义一个幸运数
#  如果输入的数字大于幸运数 提示
#  如果数字小于幸运数   提示
#  如果猜对了直接提示恭喜中奖了

i = 0
# 补全语法完整  没有任何语义
lucky_num = 6

while i < 3:
	num = input('请输入幸运数字:\n')
	# 将 输入的数字 转化整形
	int_num = int(num)
	if int_num > lucky_num:
		print('你有点大哦!!!')
	elif int_num < lucky_num:
		print('你有点小哦')
	else:
		print('恭喜你中奖了!!!')	
	i += 1 

print(num)
































