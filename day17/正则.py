import re

s = 'abcabcabcaaaab'
# 参数 正则表达式
# 参数2  表示要匹配的字符串

# li = re.findall('ab', s)
# print(li)


def rever_num(num):
    if num <= 0:
        return 0
    else:
        print(num % 10)
        return rever_num(num // 10)


if __name__ == '__main__':
    rever_num(10)
