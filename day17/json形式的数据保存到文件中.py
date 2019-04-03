import json
import os

# 将数据以json数据的行保存到文件中
REGISTER_FILE = os.path.join(os.getcwd(), 'register.txt')

TEST_FILE = os.path.join(os.getcwd(), 'test.txt')


# 将json数据保存到文件中
def register(name, password, email):
    if name and password and email:
        user = {'name': name, 'password': password, 'email': email}
        data = json.dumps(user)
        with open(REGISTER_FILE, mode='w', encoding='utf8') as f:
            f.write(data)


# 从文件中加载json数据
def load_data():
    with open(REGISTER_FILE) as file:
        data = file.read()
        user = json.loads(data)
        print(type(user))
        print(user)


def test():
    # 将json数据直接保存到文件中
    # json.dump()
    data = {'name': '宝宝'}
    with open(TEST_FILE, mode='w', encoding='utf8') as file:
        # 表示不是用模式的ascii吗
        json.dump(data, file, ensure_ascii=False)


def test1():
    with open(TEST_FILE, encoding='utf8') as file:
        # 从文件提取json数据转化成对象
        data = json.load(file)
        print(data)


if __name__ == '__main__':
    # name = input('请输入用户名:\n')
    # password = input('请输入密码:\n')
    # email = input('请输入邮箱\n')
    # register(name, password, email)
    # load_data()
    # test()
    test1()
