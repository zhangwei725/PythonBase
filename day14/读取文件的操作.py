"""
1> 打开文件
2> 读写文件中的内容
3> 关闭文件
"""
text_path = r'D:\work\PycharmProjects\wh1901\PythonBase\day14\test.txt'

# f = None
# try:
#     f = open(text_path, encoding='utf-8')
#     data = f.read()
#     print(data)
# except:
#     pass
# finally:
#     if f:
#         f.close()
image_path = r'D:\work\PycharmProjects\wh1901\PythonBase\day14\55.jpg'


# 格式二
#  with 是关键字  as 文件对象
def read_file_all():
    with open(image_path, mode='rb') as file:
        data = file.read()
        print(data)


#    读写追加 文本文件
#    读写追加  二进制文件


def read_line_file():
    """
    只读取一行的文本文件
    :return:
    """
    with open(text_path, encoding='utf8') as f:
        """
        参数  size  一次性读取文件的大小(通过情况下直接让他读取到末尾)
        """
        line = f.readline()
        print(line)


"""
一次性读取多行文件数据
返回 列表

"""


def read_lines_file():
    with open(text_path, encoding='utf-8') as file:
        text_lines = file.readlines()
        print(text_lines[0:2])

        print(type(text_lines))
        for line in text_lines:
            print(line)


text_aaa_path = r'D:\work\PycharmProjects\wh1901\PythonBase\day14\aaa.txt'


# 1字节 = 字母
#
# 演示读取的参数size
def read_size_file():
    with open(text_aaa_path, encoding='utf-8') as file:
        data = file.read(3)
        print(data)


def read_size_china_file():
    with open(text_path, encoding='utf-8') as file:
        data = file.read(6)
        print(data)


if __name__ == '__main__':
    # read_lines_file()
    # read_size_file()
    read_size_china_file()
