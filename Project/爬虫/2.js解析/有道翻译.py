# 纯python实现

import requests
import hashlib
import time
import random
import json


class YouDao(object):

    def __init__(self, word):
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.headers = {
            "Cookie": "OUTFOX_SEARCH_USER_ID=-668345552@10.169.0.82; JSESSIONID=aaabu2NTjtebx7pH5LZqx; OUTFOX_SEARCH_USER_ID_NCOO=623437081.0462145; ___rl__test__cookies=1598601592573",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63"
                        }
        self.word = word
        self.formdata = None

    def getformdata(self):
        """
        ts: r = "" + (new Date).getTime(),

        salt: r + parseInt(10 * Math.random(), 10,
        sign: n.md5("fanyideskweb" + e + i + "]BjuETDhU)zqSxf-=B#7m")
        """
        lts = str(int(time.time() * 1000))
        salt = lts + str(random.randint(0, 9))
        hs = "fanyideskweb" + self.word + salt + "]BjuETDhU)zqSxf-=B#7m"
        md5 = hashlib.md5()
        md5.update(hs.encode())
        sign = md5.hexdigest()
        self.formdata = {
            "i": self.word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": lts,
            "bv": " 16575bed92cc14c9d1dbf6a38f05ad86",
            "doctype": " json",
            "version": " 2.1",
            "keyfrom": " fanyi.web",
            "action": " FY_BY_REALTlME"
        }

    def getData(self):
        response = requests.post(self.url, headers=self.headers, data=self.formdata)
        return response.content

    def jonsData(self, data):
        translat = json.loads(data)
        fanyi = translat["translateResult"][0]
        print(fanyi)

    def main(self):
        # url
        # headers
        # formdata
        self.getformdata()
        # 发送请求，获取数据
        data = self.getData()
        # print(data)
        # 解析数据
        self.jonsData(data)


if __name__ == '__main__':
    text = input('输入内容：')
    youdao = YouDao(text)
    youdao.main()
