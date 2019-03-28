from datetime import datetime
import random

# 文本
# 文件文件的复制
copy_file_path = r'D:\work\PycharmProjects\wh1901\PythonBase\day14\aaa.txt'
new_file_path = r'D:\work\PycharmProjects\wh1901\PythonBase\day14\dddd.txt'


def copy_text_file():
    # 先读取要复制的文本文件
    with open(copy_file_path, mode='r', encoding='utf8') as read_file:
        data = read_file.read()
        with open(new_file_path, mode='w', encoding='utf8') as copy_file:
            copy_file.write(data)


# 复制多媒体
# 读写 一体  with open() as  file ,  open() as f,
# 注意: 读写的文件对象写在一行
#       使用了相对路径 默认如果没有没有盘符就直接在当前模块下面找文件
#
def copy_img_file():
    with open('55.jpg', mode='rb') as read_img_file, \
            open('imgs/new_55.jpg', mode='wb') as new_img:
        data = read_img_file.read()
        new_img.write(data)


# 写的时候配合os模块使用(动态的去获取,动态去创建)
import os


# 获取当前模块的的image目录
#  文件是动态获取
#   读二进制的数据 wb rb
def copy_file_and_os():
    img_path = os.path.join(os.path.dirname(__file__), 'image/01b01.jpg')
    new_img_path = os.path.join(os.path.dirname(__file__), 'image/1111.jpg')
    # 判断文件或者目录是否存在
    if os.path.exists(img_path):
        with open(img_path, mode='rb') as old_img, open(new_img_path, mode='wb') as new_img:
            # 二进制文件的赋值
            new_img.write(old_img.read())


# 时间模块
# 写入文件的时候 要求文件名称按着指定格式进行命名  20190101131230
# file_list = os.listdir()
# for file in file_list:
#     if os.path.isfile(file):
# 获取根目录
BASE_DIR = os.getcwd()
# 获取当前程序根目录下的image目录
IMAGE_DIR = os.path.join(BASE_DIR, 'image')


def copy_image():
    # D:\work\PycharmProjects\wh1901\PythonBase\day14\image\011313211.
    # b01.jpg
    img_path = os.path.join(IMAGE_DIR, '01b01.jpg')
    file_name = get_file_name(img_path)
    # 防止以后用户上传的时候图片名称重复导致图片丢失
    new_image_file = os.path.join(IMAGE_DIR, file_name)
    with open(img_path, mode='rb') as old_image, open(new_image_file, mode='wb') as new_img:
        new_img.write(old_image.read())
        

# 通过路径获取文件的名称
def get_file_name(img_path):
    # 获取当前文件的后缀名
    suffix_name = os.path.splitext(img_path)[-1]
    print(suffix_name)
    # 获取当前服务器的时间转化字符串
    new_name = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(100000, 999999)) + suffix_name
    return new_name


if __name__ == '__main__':
    # copy_text_file()
    # copy_img_file()
    # copy_file_and_os()
    copy_image()
