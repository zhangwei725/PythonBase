"""
1> 打开文件
2> 读写文件中的内容
3> 关闭文件
"""
write_text_path = r'D:\work\PycharmProjects\wh1901\PythonBase\day14\ccc.txt'
"""
会覆盖的写
追加 写
如果写入的不存在?  要么就创建, 操作

# 注意,写文件时一定要修改读写模式

"""


def write_text_to_file():
    s = '宝宝是一个好孩子'
    with open(write_text_path, mode='w', encoding='utf8') as file:
        file.write(s)


write_lines_text_path = r'D:\work\PycharmProjects\wh1901\PythonBase\day14\writ_lines.txt'


def write_lines_to_file():
    with open(write_lines_text_path, mode='w', encoding='utf8') as file:
        text_list = ['aaaa', 'bbb', 'python']
        # file.writelines(text_list)
        file.write(''.join(text_list))


write_mode_text_path = r'D:\work\PycharmProjects\wh1901\PythonBase\day14\writ_mode.txt'


def test_write_mode():
    # with open(write_mode_text_path, mode='r+', encoding='utf8') as file:
    #     # 测试 r+   可读可写 不创建文件
    #     file.write('测试数据')

    with open(write_mode_text_path, mode='a+', encoding='utf8') as file:
        # 测试 a+   可读可写追加
        file.write('测试数据')


if __name__ == '__main__':
    # write_text_to_file()
    # write_lines_to_file()
    test_write_mode()
