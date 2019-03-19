# 判断字符串如果包含字母h终止循环输入该字母
s = 'hello'
# debug

for  item in s:
	if item == 'h':
		print(item)
		break
		# 这个代码永远都不会被执行
		# print(item)
	else:
		print(item)
		
print(1111111)		

# 过滤h字母
# 
# 作用  终止当前这次循环进入下一次循环
# 


for l in 'Python':
	if l =='h':
		continue
	print(l)	

