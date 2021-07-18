import scrapy
from AQI.items import AqiItem


class AqiSpider(scrapy.Spider):
    name = 'aqi'
    allowed_domains = ['aqistudy.cn']
    start_urls = ['https://www.aqistudy.cn/historydata/']

    def parse(self, response, **kwargs):
        # 获取城市的url列表
        city_list = response.xpath('//div[@class="all"]/div[2]/ul/div[2]/li/a/@href').extract()

        # 遍历列表
        for url in city_list[30:32]:
            city_url = response.urljoin(url)

            # 发起城市页面请求
            yield scrapy.Request(city_url, callback=self.parse_month)

    # 解析详细页面响应
    def parse_month(self, response):
        # 获取每月详细页面的url
        month_url = response.xpath('//ul[@class="unstyled1"]/li/a/@href').extract()

        # 遍历url
        for li in month_url[50:51]:
            url = response.urljoin(li)

            # 发送详细页面的请求
            yield scrapy.Request(url, callback=self.parse_day)

    # 解析详细页面
    def parse_day(self, response):
        # 获取所有的数据节点
        day = response.xpath('//tr')
        city = response.xpath('//*[@id="title"]/text()').extract_first()

        # 遍历
        for tr in day:
            item = AqiItem()
            item['name'] = city
            item['time'] = tr.xpath('./td[1]/text()').extract_first()
            item['aqi'] = tr.xpath('./td[2]/text()').extract_first()
            item['level'] = tr.xpath('./td[3]/text()').extract_first()
            item['Pm2_5'] = tr.xpath('./td[4]/text()').extract_first()
            item['Pm10'] = tr.xpath('./td[5]/text()').extract_first()
            item['So2'] = tr.xpath('./td[6]/text()').extract_first()
            item['Co'] = tr.xpath('./td[7]/text()').extract_first()
            item['No2'] = tr.xpath('./td[8]/text()').extract_first()
            item['O3_8h'] = tr.xpath('./td[9]/text()').extract_first()

            # 返回item
            yield item
