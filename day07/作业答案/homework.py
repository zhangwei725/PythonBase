def count_str(str):
    nums = 0
    letters = 0
    spaces = 0
    others = 0
    if str:
        for l in str:
            # 判断数字
            if l.isdigit():
                nums += 1
            #     判断字母
            elif l.isalpha():
                letters += 1
            elif l.isspace():
                spaces += 1
            else:
                others += 1
    return nums, letters, spaces, others


USERNAME = 'jiaojiao'

PASSWORD = '123456'


def login():
    i = 3
    while i:
        name = input('请输入用户名:\n')
        pwd = input('请输入密码:\n')
        if name == USERNAME and pwd == PASSWORD:
            return {'name': name, 'pwd': pwd}
        else:
            i -= 1
            if i != 0:
                print('您还有{}次的重试机会'.format(i))
                continue
            break


def sum_str(*args):
    num = 0
    s = ''
    for arg in args:
        if isinstance(arg, int):
            num += arg
        elif isinstance(arg, str):
            s += arg
    return num, s


if __name__ == '__main__':
    #         统计字符串
    # print(count_str('1safsfsfs1%34646f,s df sa fs'))
    # 登录功能
    # login()
    nums, s = sum_str(1, 2, 3, 4, 5, 'ab', 'c', 'd')
    print(nums, s)
