class BankCard:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def add_money(self, num):
        if num > 0:
            self.money += num

    def del_money(self, num):
        if num <= self.money:
            self.money -= num

    def transfer_money(self, num, card):
        if card.name and self.money > 0 and num < self.money:
            self.del_money(num)
            card.add_money(num)


# 多继承
# 线程 进程 协程
class Emp:
    def __init__(self, name, dept_name, hiredate):
        # 员工姓名
        self.name = name
        # 部门名称
        self.dept_name = dept_name
        self.hiredate = hiredate


class Company:
    def __init__(self, name, dept_dict):
        #  公司的名称
        self.name = name
        # 部门的字典 {'技术部':[emp,emp],'公关部':[emp,emp]}
        self.dept_dict = dept_dict

    def add_emp(self, emp):
        """
        首先员工姓名和入职时间不能同时重复。
        如果添加的员工所在部门不存在，你需要帮他创建该部门，
        并且把他加入到该部门中，如果存在直接加入该部门即可。
        :param emp:
        :return:
        """
        # [[emp,emp],[emp,emp]]
        if self.dept_dict:
            dept_values = self.dept_dict.vaules()
            for emp_list in dept_values:
                # 获取部门中的员工信息
                for temp_emp in emp_list:
                    # 如果员工入职时间跟员工名称不同时存在,添加员工的操作
                    if not (temp_emp.name == emp.name and temp_emp.hiredate == emp.hiredate):
                        # 字段 in 用法 默认是 判断key是否存在
                        if emp.dept_name in self.dept_dict:
                            emps = self.dept_dict.get(emp.dept_name)
                            emps.append(emp)
                        else:
                            self.dept_dict[emp.dept_name] = [emp]
        else:
            # 如果公司没有任何员工
            self.dept_dict[emp.dept_name] = [emp]

    def show_company(self):
        pass


# 测试银行转账
def test_bank_card():
    liuchuan = BankCard(name='刘川', money=100000000.00)
    baobao = BankCard(name='宝宝', money=10.00)
    liuchuan.transfer_money(num=100, card=baobao)
    print(liuchuan.money)
    print(baobao.money)


def test_company():
    # 创建员工
    zuo = Emp(name='左勇杰', dept_name='舔狗部', hiredate='2019-08-05')
    ma = Emp(name='马化腾', dept_name='酱油部', hiredate='2019-08-05')
    zhao = Emp(name='赵丽颖', dept_name='影视部', hiredate='2019-08-05')
    wang = Emp(name='王凡', dept_name='公关部', hiredate='2019-08-05')

    ali = Company(name='阿里巴巴', dept_dict={})
    ali.add_emp(wang)
    ali.add_emp(zuo)
    ali.add_emp(ma)
    ali.add_emp(zhao)


if __name__ == '__main__':
    # test_bank_card()
    test_company()
