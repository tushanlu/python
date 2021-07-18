import requests
from lxml import etree


class Tieba(object):
    def __init__(self, name):
        self.url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8'.format(name)

        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'}

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def parse_data(self, data):
        # 创建element对象
        # 使用谷歌浏览器时，放开 replace， ie 则不需要
        data = data.decode().replace("<!--", "").replace("-->", "")
        html = etree.HTML(data)
        el_list = html.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')
        data_list = []
        for li in el_list:
            li_dict = {}
            li_dict['title'] = li.xpath('./text()')[0]
            li_dict['link'] = 'https://tieba.baidu.com/' + li.xpath('./@href')[0]
            data_list.append(li_dict)
        # 获取下一页url
        try:
            next_url = 'https:' + html.xpath("//a[contains(text(), '下一页>')]/@href")[0]
        except:
            next_url = None
        print(next_url)
        return data_list, next_url

    def save_data(self, data_list):
        for data in data_list:
            print(data)

    def run(self):
        # url
        # headers
        next_url = self.url
        while True:
            # 发送请求，获取响应
            data = self.get_data(next_url)
            # 从响应中提取数据
            data_list, next_url = self.parse_data(data)
            self.save_data(data_list)
            # 判断是否停止
            if next_url == None:
                break


if __name__ == '__main__':
    tieba = Tieba('刀剑神域')
    tieba.run()
