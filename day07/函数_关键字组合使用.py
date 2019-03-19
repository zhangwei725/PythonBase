"""
1> 声明 变量 nonlocal 跟局部变量绑定  使用global声明全局变量
变量查找的顺序   先局部 在全局

"""
"""
开发 40 debug 50%
对于初级程序锻炼代码逻辑的一个神器,
找出程序bug的重要的技能

"""

"""
第一步 必须使用debug运行程序
第二步 在程序中打断点  在有效代码上打断点

"""


def outer(num):
    def inner_local():
        num = 10

    def inner_nonlocal():
        nonlocal num
        num = 20

    def inner_global():
        global num
        num = 30

    # 第一行
    # print(num)  # 50
    inner_local()
    # print(num)  # 50
    inner_nonlocal()
    # print(num)  # 20
    inner_global()
    # 20
    # print(num)

outer(50)



def test():
    print()


# 程序入口函数
# def main():
#     outer(50)
#     test()

# 理解程序入口

if __name__ == "__main__":
    # 程序入口
    # outer(50)
    # test()
    pass
