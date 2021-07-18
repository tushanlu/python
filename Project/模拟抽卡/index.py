# 卡分别为 S R A B
# 出率分别为 1% 9% 50% 40%
# 水位机制 累计100次后抽卡后得S
# 获得S后重新计数

import random
import file
from time import sleep


class Random(object):
    def __init__(self):
        self.S = ['夕', '年', '霜星']
        self.R = ['红', '白金', '蓝毒', '巫恋', '陨星', '乌有']
        self.A = ['桃金娘', '红豆', '卡达', '苏苏洛', '夜烟', '红云', '子虚', '安可', '豆苗']
        self.B = ['芬', '玫兰莎', '卡缇', '克洛斯', '安赛尔', '香草', '梓兰']

    # def s(self):

    #     file.write_file('data/water level.txt',str(0))
    #     print('[S]:', random.choice(self.S))

    # def r(self):

    #     print('[R]:', random.choice(self.R))

    # def a(self):

    #     print('A:', random.choice(self.A))

    # def b(self):

    #     print('B:', random.choice(self.B))

    def random_int(self):
        card_pool = random.randint(0, 99)
        # 读取水位
        water_level = int(file.read_file('data/water level.txt'))
        file.write_file('data/water level.txt', str(water_level + 1))

        if card_pool < 1 or water_level > 98:
            file.write_file('data/water level.txt', str(0))
            self.result_card('[S]:', self.S)

        elif card_pool > 0 and card_pool < 11:
            self.result_card('[R]:', self.R)

        elif card_pool > 10 and card_pool < 60:
            self.result_card('A:', self.A)

        else:
            self.result_card('B:', self.B)

    # 显示结果
    @staticmethod
    def result_card(level, card_group):
        print(level, random.choice(card_group))

    def rnu(self):

        water_level = int(file.read_file('data/water level.txt'))
        print('剩余{}次必出S'.format(100-water_level))
        frequency = int(input('选择抽卡次数--->1次 or 10次\n-->'))
        if frequency == 1:
            # self.write_file(str(1 + water_level))
            self.random_int()
        else:
            for i in range(10):
                self.random_int()
                sleep(0.05)


if __name__ == "__main__":
    Random = Random()
    # Random.write_file(str(0))
    print('模拟抽卡系统')
    while True:
        try:
            print('<-------------------------->')
            Random.rnu()

        except:
            print('退出系统')
            break
