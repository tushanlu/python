# 卡分别为 S R A B
# 出率分别为 2% 8% 50% 40%
# 首次十次抽卡内必获得R以上的卡（仅一次）
# 前50次未获得S S的概率+2% 依此类推 B概率降低
# 获得S后恢复初始概率 重新记数


import random
import file
from time import sleep


class Random(object):
    def __init__(self):
        self.S = ['夕', '年', '霜星']
        self.R = ['红', '白金', '蓝毒', '巫恋', '陨星', '乌有']
        self.A = ['桃金娘', '红豆', '卡达', '苏苏洛', '夜烟', '红云', '子虚', '安可', '豆苗']
        self.B = ['芬', '玫兰莎', '卡缇', '克洛斯', '安赛尔', '香草', '梓兰']
        self.r = 0
        self.s = 0
        self.up = 0
        self.s_gailv = 0

    def random_int(self):
        card_pool = random.randint(0, 99)
        # 读取水位
        water_level = int(file.read_file('data/water level2.txt'))
        file.write_file('data/water level2.txt', str(water_level + 1))

        if water_level // 50 > (0 + self.s_gailv):
            self.up += 2
            self.s_gailv += 1

        if self.r == 0 and water_level == 9:
            card_pool = random.randint(0, 9)
            if card_pool < 2:
                self.result_card('[S]:', self.S)
                file.write_file('data/water level2.txt', str(0))
                self.s += 1

            else:
                self.result_card('[R]:', self.R)
                self.r += 1

        else:
            if card_pool < (2 + self.up):
                file.write_file('data/water level2.txt', str(0))
                self.result_card('[S]:', self.S)
                self.s += 1
                self.up = 0
                self.s_gailv = 0

            elif card_pool > (1 + self.up) and card_pool < (10 + self.up):
                self.result_card('[R]:', self.R)
                self.r += 1

            elif card_pool > (9 + self.up) and card_pool < (60 + self.up):
                self.result_card('A:', self.A)

            else:
                self.result_card('B:', self.B)

    # 显示结果

    @staticmethod
    def result_card(level, card_group):
        print(level, random.choice(card_group))

    def rnu(self):

        water_level = int(file.read_file('data/water level2.txt'))
        if water_level < 10 and self.r == 0:
            print('剩余{}次必出R以上'.format(10-water_level))
        frequency = int(input('选择抽卡次数--->1次 or 10次\n-->'))
        if frequency == 1:
            # self.write_file(str(1 + water_level))
            self.random_int()
        else:
            for i in range(10):
                self.random_int()
                sleep(0.05)
        print('**获得R的卡{}张**'.format(self.r))
        print('**获得S的卡{}张**'.format(self.s))


if __name__ == "__main__":

    Random = Random()
    file.write_file('data/water level2.txt', str(0))
    print('模拟抽卡系统')
    while True:
        try:
            print('<-------------------------->')
            Random.rnu()

        except:
            print('退出系统')
            break
