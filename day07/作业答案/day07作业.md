第一步

课堂代码敲一遍

第二歩 编程题

1. 写函数，计算传入字符串中的数字、字母、空格和其他的个数

   ```python
   def count_str(str):
       nums = 0
       letters = 0
       spaces = 0
       others = 0
       if str:
           for l in str:
               # 判断数字
               if l.isdigit():
                   nums += 1
               #     判断字母
               elif l.isalpha():
                   letters += 1
               elif l.isspace():
                   spaces += 1
               else:
                   others += 1
       return nums, letters, spaces, others
   ```

2. 普通参数、默认值参数、可变长度参数、可变长度关键字参数的区别

3. 请说出函数的作用域有哪些,他们的范围是啥,查找规则是啥

4. 编写函数封装注册功能接受参数用户名,密码,邮箱

5. 函数实现登录功能,要求如下
   1. 接受用户名密码
   2. 如果密码输入错误,提示重试次数,如果连续三次输入密码错误直接退出,并提示24小时之后才能重试

   ```python
   USERNAME = 'jiaojiao'
   
   PASSWORD = '123456'
   
   
   def login():
       i = 3
       while i:
           name = input('请输入用户名:\n')
           pwd = input('请输入密码:\n')
           if name == USERNAME and pwd == PASSWORD:
               return {'name': name, 'pwd': pwd}
           else:
               i -= 1
               if i != 0:
                   print('您还有{}次的重试机会'.format(i))
                   continue
               break
   ```

6. 传入多个参数(数字和字符串)，如果是数字累加和，如果是字符串进行拼接。

   ```python
   def sum_str(*args):
       num = 0
       s = ''
       for arg in args:
           if isinstance(arg, int):
               num += arg
           elif isinstance(arg, str):
               s += arg
       return num, s
   ```

   

