# for 循环专门用于遍历序列

# li = ['宝宝', '武汉市', 18, 10.00]

# for item in li:
#     print(item)

#
li = [1, 2, 3, [4, 5]]
# 给定列表 将列表中所有的元素全部打印
count = 1
for item in li:
    if count == 4:
        for it in item:
            print(it)
    else:
        print(item)
    count += 1



