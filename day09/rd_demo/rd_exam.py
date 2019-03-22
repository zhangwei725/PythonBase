import random
import time

if __name__ == '__main__':
    # print('产生一个0-1之间的随机数{}'.format(random.random()))
    # print('指定范围{}'.format(random.uniform(10, 15)))
    print('指定范围的整数{}'.format(random.randint(1000, 10000)))
    # print('指定范围,默认自增{}'.format(random.randrange(1, 1000)))
    r = random.choice([4, 5, 6, 7, 8, 9, 'a', 'b', 'c'])
    print('从指定的序列中获取随机元素{}'.format(r))
