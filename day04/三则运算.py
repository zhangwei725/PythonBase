# 如果年龄小于16,你祖国的花朵,如果大于16,你就是老腊肉
#  ctrl + alt + L  快速格式化
input_age = input('请输入你的年龄:\n')
age = int(input_age)
# 简单的只有一句代码的if在赋值的时候可以使用三则运算的语法
if age > 16:
    print('你祖国的花朵')
else:
    print('你就是老腊肉')
#  值 if  布尔表达式   else  值
#   如果布尔表达式为True  则 返回if前面的值  否则返回 else后面的值
name = '你祖国的花朵' if age <= 16 else '你就是老腊肉'

print(name)

# 输入两个数
# 如果第一个数大于0 返回第一个数,否则返回第二个数
# 第一种方式使用 if else
# 第二种方式   and   or
input_num1 = int(input("请输入第一个数"))
input_num2 = int(input("请输入第二个数"))
num = input_num1 if input_num1 > 0 else input_num2
# 比较两个数的大小
# num = input_num1 if input_num1 > input_num2 else input_num2
# 多元赋值
x, y = 1, 2
# num = (x > y and x) or (x < y and y)
# print(num)
