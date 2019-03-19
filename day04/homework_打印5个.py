count = 0

for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 != 0):
        count += 1
        # 每个数重新换行
        if count % 5 == 0:
            print(i)
        else:
            print(i, end=',')

print('总数是多少%s' % count)
