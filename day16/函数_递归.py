# 递归最大的次数不超过1000次,如果递归的次数超过这个数 RecursionError: maximum recursion depth exceeded
# 修改递归最大的次数

# import sys
# sys.setrecursionlimit(10000)

# 递归

#   1 * 2 * 3

# def mul(num):
#     result = 1
#     for i in range(2, num + 1):
#         result *= i
#     return result
#
#
# print(mul(3))


# 1 * 2 * 3...
def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n - 1)


"""
1>  5 * func(4)
2>  5 * 4 *func(3)
3>  5 * 4 * 3 func(2)
4>  5 * 4 * 3 * 2 * 1

"""

"""
遍历当前目录下所有的文件
"""

import os

# 遍历目录中的文件和文件夹
#
"""
必要 参数top  要遍历的根目录
参数topdown  优先遍历子目录
参数onerror   当遍历发生错误的时候回调一个函数
followlinks=False  是否遍历目录下的快捷方式,默认是关闭


返回值
root 根目录 
filedir 文件的目录
filename  文件名

"""

print(func(10))
# 文件递归
import os


# 生成器, 迭代 列表
def iter_files(root):
    # 打印所有文件的完整路径
    for dir, file_dir, file_names in os.walk(root):
        for file_name in file_names:
            print(os.path.join(dir, file_name))


def iter_dirs(root):
    dirs = os.listdir(root)
    for dir in dirs:
        if os.path.isdir(dir):
            # 获取子目录的路径
            child_path = os.path.join(root, dir)
            iter_dirs(child_path)
        else:
            # 对文件进行过滤 (.txt)
            if os.path.splitext(dir)[-1] == '.txt':
                print(dir)


# 递归实现列表的倒序
# 算出长度  算出索引将最后一个元素放在第一个
# 终止条件    长度小于0
def reversed_list(li, new_list):
    # 终止条件
    if 0 >= len(li):
        return new_list
    else:
        new_list.append(li.pop(-1))
        return reversed_list(li, new_list)


if __name__ == '__main__':
    # root_dir = r'D:\work\PycharmProjects\wh1901\PythonBase\day14'
    # iter_files(root_dir)
    # iter_dirs(root_dir)

    li = [1, 2, 3, 4, 6, 5,9]
    # 直接使用内置函数 reversed
    # print(list(reversed(li)))
    new_list = []
    print(reversed_list(li, new_list))
