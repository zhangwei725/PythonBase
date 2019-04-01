"""
假设
我需要一个函数，接收2个参数，分别为方向(direc棋盘大小为50*50，左上角为坐标系原点(0,0)，我需要一个函数，接收2个参数，分别为方向(direction)，步长(step)，
该函数控制棋子的运动。棋子运动的新的坐标除了依赖于方向和步长以外，
当然还要根据原来所处的坐标点，
用闭包就可以保持住这个棋子原来所处的坐标。
"""

#
# 系统已经没有内存可以给你使用了    内存泄露

# 系统只分配给你100m内存,101M       内存溢出


def start_game(direction, step):
    # 原点坐标
    origin_position = [0, 0]
    # x最大坐标
    x_max_position = [0, 50]
    # y最大坐标
    y_max_position = [0, 50]
    """
    [-1,1]
    [-1,1]
    方向    x 轴方向 -1表示反向  1表示正方向  y轴方法 [1,0]
    
    """

    def player(direction, step):
        new_x = origin_position[0] + direction[0] * step
        new_y = origin_position[1] + direction[1] * step
        origin_position[0] = new_x
        origin_position[1] = new_y
        print(origin_position)

    return player


if __name__ == '__main__':
    # player = start_game()
    # player(direction=[1, 0], step=1)
    # player(direction=[0, 1], step=2)
    start_game(direction=[1, 0], step=1)
    start_game(direction=[0, 1], step=2)
