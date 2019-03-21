# 快捷键  万能键  alt + 回车
# 快速导入包   1 选中需要导入的方法或者变量  2 alt + 回车  3 选择 import
# 注意事项 不要使用 from ... import *  禁用  import *


from day08.from2 import *

if __name__ == '__main__':
    # 程序入口
    user = register('python', '123', '1000@qq.com')
    print(user)
    print(li)
    login()
