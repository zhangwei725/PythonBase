from day08.work.dept import add_emp, del_emp, find_emp


def test_add():
    # 测试 添加功能
    add_emp(phone='110', name='宝宝1号', job='IT')
    add_emp(phone='1101', name='宝宝2号', job='IT')
    add_emp(phone='110', name='宝宝3号', job='IT')


def test_del():
    name = input('请输入姓名者工号或手机号')
    if del_emp(name):
        print('删除成功')
    else:
        print('删除失败')


def test_find():
    name = input('请输入姓名或者手机号或者职位:\n')
    is_find = find_emp(name, 1)
    if is_find:
        print(is_find)
    else:
        print('查无此人')


if __name__ == '__main__':
    test_add()
    # test_del()
    test_find()
