import time as  t
from datetime import date, time, datetime, timedelta


def date_examp():
    # date_ = date(year=2019, month=9, day=11)
    # print(type(date_))
    # 获取系统当前的日期
    date_obj = date.today()
    print(date_obj.year, date_obj.month, date_obj.day)
    # time
    # 等价于 兼容 2.x版本
    # print(date.fromtimestamp(t.time()))


def time_examp():
    t = time(12, 2, 3, 1)
    print(t.hour, t.minute, t.second, t.microsecond)
    print(t.strftime('%H:%M:%S'))
    print(type(t))


#
def datetime_examp():
    # 创建时间日期对象
    # dt = datetime(year=2019, month=3, day=21, hour=18)
    # print(dt)
    # 获取当前系统的时间
    # 获取当前的年月日时分秒微秒
    today = datetime.today()
    print(today)
    # 这个方法在开发中用的居多
    # now = datetime.now()
    # print(type(now))
    # print(now)
    # 将datetime类型转化成字符串类型(指定格式输出)
    # now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print(type(now_str))
    # print(now_str)
    # 将指定的字符串格式类型转化成datetime类型
    dt = datetime.strptime('2019-03-21 14:17:27', '%Y-%m-%d  %H:%M:%S')
    print(dt)


# 时间间隔
"""
weeks   7天
days 
seconds
milliseconds 1毫秒 = 1000微秒
microseconds  
minutes
hours

"""


def timedelta_examp():
    # 创建时间差对象
    print(timedelta(days=1))
    """
    常用操作
    + 
    -
    * 
    / //
    比较
    """
    td1 = timedelta(hours=1)
    td2 = timedelta(hours=2)
    td3 = td1 + td2
    print(td3.seconds)

    td4 = td2 - td1
    print(td4.seconds)
    td5 = td1 * 3
    print(td5.seconds)
    print(td1 > td2)
    print(td1 == td2)


import pytz


#  'Asia/Shanghai' 亚洲上海
def pytz_examp():
    tz = pytz.timezone('Asia/Shanghai')
    print('上海时间:%s' % datetime.now(tz))
    tz1 = pytz.timezone('US/Alaska')
    print('美国时间%s' % datetime.now(tz1))


# sys
# os
# random
# 异常

#  线程    进程  协程

if __name__ == '__main__':
    pass
    # date_examp()
    # time_examp()
    # datetime_examp()
    # timedelta_examp()
    pytz_examp()
