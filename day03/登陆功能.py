account  =  input('请输入账号或者手机号:\n')
password = input('请输入密码:\n')

# 在复杂的程序无非就多了几个if else


# 账号密码不能为空

if account  and password:
	if  (account == 'xm123' or account == '110') and password == '123':
		print('登陆成功!!!')
	else:
		print('登陆失败')	
else:
	print('账号密码不能为空')








