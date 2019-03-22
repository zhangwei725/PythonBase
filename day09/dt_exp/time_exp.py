import time
import datetime

import pytz

#  'Asia/Shanghai' 亚洲上海

if __name__ == '__main__':
    # 1553137555.8185785
    # 获取时间戳
    print(time.time())
    #     获取时间元组
    # struct = time.localtime()
    # print(struct)
    # 夏令时
    # 0 - 6 (0 周一  1 周二  2 周三 3 周四  4 周五  5 周六 )

    # print(time.asctime(time.localtime()))
    # 将时间转化成指定格式输出(五星)
    # print(time.strftime('%Y%m-%d %H:%M:%S', time.localtime()))
    # print(time.strftime('%Y-%m-%d', time.localtime()))
    # print(time.strftime('%H:%M:%S', time.localtime()))
    #    相互之间转化
    #
    # time_str = '2019-11-11 13:30:50'
    # print(type(time.localtime()))
    # struct_time = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    # print(
    #     struct_time
    # )
    # timestamp = time.mktime(struct_time)
    # print(timestamp)
    # date_str = input('请输入日期')
    # time.sleep(24 * 60 * 60)
    # time.sleep(0.6)
