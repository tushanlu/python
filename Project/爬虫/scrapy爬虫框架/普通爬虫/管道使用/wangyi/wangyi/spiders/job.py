import scrapy
from wangyi.items import WangyiItem


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do?postType=01']

    def parse(self, response, **kwargs):
        # 提取数据

        node_list = response.xpath('*//tbody/tr')
        # print(len(node_list))
        for num, node in enumerate(node_list):
            if num % 2 == 0:
                item = WangyiItem()
                item['name'] = node.xpath('./td[1]/a/text()').extract_first()
                # response.urljoin()用于拼接相对路径的url
                item['link'] = response.urljoin(node.xpath('./td[1]/a/@href').extract_first())
                item['depart'] = node.xpath('./td[2]/text()').extract_first()
                item['category'] = node.xpath('./td[3]/text()').extract_first()
                item['type'] = node.xpath('./td[4]/text()').extract_first()
                item['address'] = node.xpath('./td[5]/text()').extract_first()
                item['num'] = node.xpath('./td[6]/text()').extract_first().strip()
                item['data'] = node.xpath('./td[7]/text()').extract_first()
                # yield item

                # 构建详情页面的请求
                yield scrapy.Request(url=item['link'], callback=self.parsr_detail, meta={'item': item})

            # 翻页
            parturl = response.xpath('/html/body/div[2]/div[2]/div[2]/div/a[last()]/@href').extract_first()

            # 判段终止条件
            if parturl != 'javascript:void(0)':
                nexturl = response.urljoin(parturl)
                # 构建请求对象，返回给引擎
                yield scrapy.Request(url=nexturl, callback=self.parse)    # 默认使用parse

    def parsr_detail(self, response):
        # 将meta传参获取
        itme = response.meta['item']
        # print("--------",itme)

        # 提取剩余字段数据
        itme['duty'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/text()').extract()
        itme['require'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/text()').extract()

        # 返回给引擎
        yield itme
