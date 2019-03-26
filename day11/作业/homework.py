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


"""
字典  列表   对象
"""


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
    """

    """

    def __init__(self, name, dept_dict):
        #  公司的名称
        self.name = name
        # 部门的字典 {'技术部':[emp,emp],'公关部':[emp,emp]}
        self.dept_dict = dept_dict

    """
    模仿  --- 写简单的案例 ----   复杂程序
    """

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
            # 如果员工存在则直接返回
            if self.is_exist(emp):
                return
            # 如果所在部门存在 则直接添加员工到列表
            if emp.dept_name in self.dept_dict:
                #  通过key获取字典员工列表
                emps = self.dept_dict.get(emp.dept_name)
                # 将员工添加到列表中
                emps.append(emp)
            else:
                # 如果部门不存在 则直接添加部门和员工
                self.dept_dict[emp.dept_name] = [emp]
                # 如果添加完成,就终止循环,结束方法
        else:
            # 如果公司没有任何员工
            self.dept_dict[emp.dept_name] = [emp]

    def show_company(self):
        pass

    def is_exist(self, emp):
        """
        用于判断员工是否存在,
        :return: 如果返回True 表示员工存在,则无需添加员工, 如果返回False 表示员工不存在
        """
        # 获取部门字典中所有的员工列表
        dept_values = self.dept_dict.values()
        for emp_list in dept_values:
            # 获取部门中的员工信息
            for temp_emp in emp_list:
                # 如果员工入职时间跟员工名称不同时存在,添加员工的操作
                if temp_emp.name == emp.name and temp_emp.hiredate == emp.hiredate:
                    print('员工的信息已录入,不能添加')
                    #
                    return True
        return False


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
    ma = Emp(name='左勇杰', dept_name='舔狗部', hiredate='2019-08-05')
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
