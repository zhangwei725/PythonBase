import os


def base():
    """
     os 基础操作
    :return:
    """
    # nt windows
    # posix  Linux  Unix  或者 mac os
    print(os.name)
    #  获取的是操作系统的详细信息
    # print(os.uname())
    #     获取操作系统中的环境变量
    print(os.environ)
    # 获取当前目录(.)
    print(os.curdir)
    # 获取当前文件的目录
    print(os.getcwd())
    # 获取指定目录下所有的文件和目录
    # 可读 可写  可执行
    print(os.listdir(os.getcwd()))
    #     创建目录
    """
        path  要创建的目录
        mode   权限 
        
    注意:一定要保证创建目录的根目录存在
    """
    # path = r'D:\work\PycharmProjects\wh1901\PythonBase\os_demo\1'
    # os.mkdir(path)
    # 拼接路径
    rm_path = os.getcwd() + '\\' + '1'
    # 删除指定的空目录
    os.rmdir(rm_path)
    os.remove(r'D:\work\PycharmProjects\wh1901\PythonBase\os_demo\2\hehe.py')

if __name__ == '__main__':
    base()
