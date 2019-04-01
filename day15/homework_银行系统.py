import time
import random


class User:
    def __init__(self, name, no, phone, card):
        self.name = name
        self.no = no
        self.phone = phone
        self.card = card


class Card:
    def __init__(self, password, balance):
        self.card_no = random.randint(62000000000, 62999999999)
        self.password = password
        # 余额
        self.balance = balance
        # 0 表示销户 1表示正常 2 表示锁卡
        self.status = 1


# 1 ,2,3,4,5
class ATM:
    CARD_FILE = 'card'

    def __init__(self):
        self.user_dict = {}

    # 开户、查询、取款、存款、转账、改密、锁定、解锁、补卡、销户
    def open_hu(self, user):
        self.user_dict[user.card.card_no] = user
        with open(ATM.CARD_FILE, mode='a', encoding='utf-8') as f:
            f.write(str(self.user_dict))

    # 查询
    def find_user(self, card_no):
        """
        :param card_no: 卡号
        :return:
        """
        if card_no in self.user_dict:
            user = self.user_dict.get(card_no)
            print('您的卡号的余额是:{}'.format(user.card.balance))
        else:
            print('卡号不存在!!!')

    # 取款
    def give_qian(self):
        pass

    # 存款
    def save_money(self):
        pass

    def transfer_money(self):
        pass

    def change_password(self):
        pass

    def lock_user(self):
        pass

    def unlock_user(self):
        pass

    def replace_card(self):
        pass

    def del_user(self):
        pass

    def is_user_exists(self):
        with open(ATM.CARD_FILE, encoding='utf8') as file:
            file.readlines()


class Admin:
    is_login = False
    # 显示管理员操作界面
    def init_sys(self):
        print('==============后台管理界面===================')
        print('==============系统启动ing...=================')
        time.sleep(1)
        print('==============loadding....===================')
        time.sleep(2)
        print('==============系统启动成功===================')

    def operation(self):
        print("=============请选择相关操作=============")
        print("************************************")
        print("*      开户(1)     查询(2)           *")
        print("*      取款(3)     存款(4)           *")
        print("*      转账(5)     改密(6)           *")
        print("*      锁定(7)     解锁(8)           *")
        print("*      销户(9)     退出(0)           *")
        print("************************************")

    # 登出
    def login(self, username, password):
        if username == 'admin' and password == '123':
            return True
        else:
            return False

    # 登出
    def logout(self):
        time.sleep(random.random())
        print('系统正在登出ing...')


def main():
    admin = Admin()
    atm = ATM()
    admin.init_sys()
    username = input('请输入管理员账号')
    password = input('请输入管理员密码')
    is_login = admin.login(username, password)
    while True:

        if is_login:
            admin.operation()
            num = int(input('请选择相关操作'))
            if num == 1:
                print('====请输入用户信息====')
                name = input('请输入用户名')
                no = input('请输入身份证号')
                phone = input('请输入手机号')
                password = input('请输入银行卡密码')
                balance = input('请输入开户金额')
                card = Card(password=password, balance=balance)
                user = User(name=name, no=no, phone=phone, card=card)
                atm.open_hu(user)
                print(user.card.card_no)
            elif num == 2:
                # 查询余额
                card_no = int(input('请输入卡号'))
                atm.find_user(card_no)
            elif num == 1:
                pass
            elif num == 1:
                pass
            elif num == 1:
                pass
            elif num == 0:
                admin.logout()
                break
            else:
                print('智商是不足,请充值...')
        else:
            print('请登录!!!')


if __name__ == '__main__':
    main()
