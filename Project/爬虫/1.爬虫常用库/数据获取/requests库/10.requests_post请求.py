# 思考：哪些地方我们会用到POST请求？
# 1.登录注册（在web工程师看来POST比GET更安全，url地址中不会暴露用户的账号密码信息）
# 2.需要传输大文本内容的时候（POST请求对数据长度没有要求）
# 所以，同样的，我们的爬虫也需要在这两个地方会去模拟浏览器发送post请求

# requests发送post请求的方法

# responsn = requests.post(url,data)

import requests
import json


class King(object):
    def __init__(self, word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.word = word
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
            }
        self.data = {"f": "auto",
                     "t": "auto",
                     "w": self.word
                    }

    def get_data(self):
        response = requests.post(self.url, data=self.data, headers=self.headers)
        return response.content

    def parse_data(self, data):
        dict_data = json.loads(data)
        try:
            print(dict_data['content']['out'])
        except:
            print(dict_data['content']['word_mean'][0])

    def run(self):
        # 编写爬虫逻辑

        # url
        # headers
        # data字典
        # 发送请求获取响应

        response = self.get_data()
        # 数据解析
        self.parse_data(response)


if __name__ == '__main__':
    word = input('输入翻译的内容:')
    king = King(word)
    king.run()
# 实现方法
# requests.post(url, data)
# data是一个字典
# post数据来源
# 1.固定值			抓包比较不变值
# 2.输入值			抓包比较根据自身变化值
# 3.预设值-静态文件	需要提前从静态html中获取
# 4.预设值-发请求		需要对指定地址发送请求
# 5.在客户端生成的		分析js，模拟生成数据





