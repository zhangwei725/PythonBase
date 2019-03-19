# 2 3
# 循环嵌套
# break的使用

# for i in range(2, 101):
#     # 假设所有的数都是质数据
#     flag = True
#     j = 2  #
#     # 如果能被其他数整除 不是一个数据
#     while j < i:  # 从2开始到前面一个数
#         if i % j == 0:
#             # 如果进入该循环就表示不是质数
#             flag = False
#             break
#         j += 1
#     if flag:
#         print(i)

for i in range(2, 101):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)

