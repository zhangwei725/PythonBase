import os


def base_path():
    # 查看当前目录的绝对路径
    # absolute 绝对
    # print(os.path.abspath('.'))
    #  拼接路径
    ""
    """
    path:  拼接的根目录
    paths:  要拼接目录
    注意:  参数2  不应该 \
    """
    root_path = r'D:\work\PycharmProjects\wh1901\PythonBase'
    # print(os.path.join(os.path.abspath('.'), r'aaa'))

    # 获取文件名加后缀名
    py_path = r'D:\work\PycharmProjects\wh1901\PythonBase\os_demo\__init__.py'
    # print(os.path.split(py_path))
    # 获取文件的后缀名
    # print(os.path.splitext(py_path)[-1])
    #     判断路径是否是目录
    # print(os.path.isdir(root_path))
    # print(os.path.isdir(py_path))
    # 判断路径是否是文件
    # print(os.path.isfile(py_path))
    # 判断文件或者目录是否存在
    root_path1 = r'D:\work\PycharmProjects\wh1901\PythonBase1'
    # print(os.path.exists(root_path1))
    #     返回当前文件所在的路径
    # print(os.path.dirname(py_path))
    # 获取当前文件所在的绝对路径
    # print(os.path.abspath(__file__))


"""
根据日期动态的创建目录 
2019/3/22/work
2019/3/23/work
"""


def demo():
    # 创建目录
    # 在当前文件所在的目录下创建  static目录下创建一个img的目录
    """
    第一步先获取当前文件所在的路基
    :return:
    """
    folder_path = os.path.dirname(os.path.abspath(__file__))
    static_folder = os.path.join(folder_path, 'static')
    if not os.path.exists(static_folder):
        os.mkdir(static_folder)

    img_folder = os.path.join(static_folder, 'img')
    if not os.path.exists(img_folder):
        os.mkdir(img_folder)
    # /
    # 显示img目录下的所有文件(要求显示绝对路径)
    # D:\work\PycharmProjects\wh1901\PythonBase\os_demo\static\img
    img_path = os.path.join(os.getcwd(), r'static\img')
    if os.path.exists(img_path):
        files = os.listdir(img_path)
        if files:
            for file in files:
                rea_file = os.path.join(img_path, file)
                if os.path.isfile(rea_file):
                    print(rea_file)


if __name__ == '__main__':
    # base_path()
    demo()
