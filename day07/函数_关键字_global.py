# global 关键
# nonlocal 3.2 +

# num +=1
# 如果说我们在函数里使用global关键声明的变量 自动提升到全局作用域
num = 0


def test(n):
    global num
    num = num + 1
    print(num)


test(1)
