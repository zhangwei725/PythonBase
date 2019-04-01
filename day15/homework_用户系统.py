# 项目的根目录
import os

# 能写  ----> 写好


# 获取项目的根目录
BASE_DIR = os.path.dirname(__file__)
#  获取保存用户注册信息根目录
REGISTER_DATA_PATH = os.path.join(BASE_DIR, 'data')
# 如果目录不存在 则创建目录
if not os.path.exists(REGISTER_DATA_PATH):
    os.mkdir(REGISTER_DATA_PATH)
# 保存注册数据文件
REGISTER_DATA_PATH_FILE = os.path.join(REGISTER_DATA_PATH, 'register')

# 界面的功能

# 显示数据  用户输入数据
"""
性能 优化
"""


class User:

    def __init__(self):
        self.username = None
        self.password = None
        self.email = None

    def __str__(self):
        return "username:{},password:{},email:{}".format(self.username, self.password, self.email)

    @staticmethod
    def login(username, password):
        users = UserManger.init()
        if username and password:
            for user in users:
                if user.username == username and user.password == password:
                    return True
        else:
            return False

    @staticmethod
    def save_to_file(username, password, email):
        flag = None
        """
        将数据保存到文件中
        :param username:
        :param password:
        :param email:
        :return:
        """
        user = 'username:{}\npassword:{}\nemail:{}\n'.format(username, password, email)
        with open(REGISTER_DATA_PATH_FILE, mode='a+', encoding='utf8') as file:
            file.write(user)
            flag = True

        return flag

    # 符合的命名规则  大写组合+数字
    # 密码规则   字母 + 数字  长度大于8

    #   注册完成之后写入文件中
    @staticmethod
    def register(username, password, email):
        if username and password and email:
            # 判断一下用户或者邮箱是否已经被注册
            # 将数据写入到文件
            flag = User.save_to_file(username, password, email)
        else:
            raise Exception('数据不符合规范,请检查后重新输入')
        return flag


class UserManger:
    users = []

    #
    # 字符串操作  文件操作   列表操作  对象操作  逻辑能力
    # 获取列表的数据
    # 3行表示一个对象
    # 0   账号信息 \n
    # 1
    # 2
    @classmethod
    def init(cls):
        with open(REGISTER_DATA_PATH_FILE, encoding='utf8') as f:
            text_list = f.readlines()
            text_list.remove('\n')
            print(text_list)
            # 通过索引获取列表中的数据
            for i in range(len(text_list)):
                if i % 3 == 0:
                    # 新对象  三行一个对象
                    # 获取用户名的数据
                    user = User()
                    # 对单行数据进行处理,  去掉换行符,空格 获取存储的用户的值
                    user.username = text_list[i].strip().split(':')[-1]
                    # 把对象加入列中
                    cls.users.append(user)
                elif i % 3 == 1:
                    # 密码
                    user.password = text_list[i].strip().split(':')[-1]
                    pass
                elif i % 3 == 2:
                    user.email = text_list[i].strip().split(':')[-1]
                    # 邮箱
        return cls.users


# 测试注册
def main():
    username = input('请输入注册的用户名:')
    password = input('请输入注册的密码:')
    email = input('请输入注册的邮箱:')
    is_register = User.register(username=username, password=password, email=email)
    if is_register:
        print('注册成功!!!')
        print('你可以观看高清的视频')
    else:
        print('注册失败!!!!')


# 测试登录
def test_login():
    username = input('用户名')
    password = input('密码')
    is_login = User.login(username, password)
    if is_login:
        print('登录成功!!!')
    else:
        print('登录失败')


if __name__ == '__main__':
    # main()
    test_login()
