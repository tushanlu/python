# -*- coding: utf-8 -*-
import scrapy
from Itcast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response, **kwargs):
        # 获取教师节点
        t_list = response.xpath('//div[@class="li_txt"]')
        # print(len(t_list))
        # 遍历教师节点
        for data in t_list:
            # itme = {}
            itme = ItcastItem()
            # xpath方法返回的是选择器对象列表,extract()用于从选择器对象中提取数据
            # extract_first()列表为空时返回None,否则返回第一个值
            itme['name'] = data.xpath('./h3/text()').extract_first()
            itme['title'] = data.xpath('./h4/text()')[0].extract()
            itme['desc'] = data.xpath('./p/text()')[0].extract()
            yield itme

