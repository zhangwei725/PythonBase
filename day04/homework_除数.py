x = 1
for x in range(1, 150):
    y = 150 - x
    if x // y == 3 and x % y == 10:
        print('被除数{}'.format(x), '除数{}'.format(y))
