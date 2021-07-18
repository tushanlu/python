import scrapy
from dangdang.items import DangdangItem

# ----1 导入分布式爬虫类
from scrapy_redis.spiders import RedisSpider


# ----2 继承分布式爬虫类
class DangSpider(RedisSpider):
    name = 'dang'

    # ----3 注销start_urls&allowed_domains
    # allowed_domains = ['dangdang.com']
    # start_urls = ['http://category.dangdang.com']

    # ----4 设置redis-key
    redis_key = 'py21'

    # ----5 设置__init__
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domain = filter(None, domain.strip(','))
        super(DangSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # 获取大分类节点
        big_node_list = response.xpath('//*[@id="floor_1"]/div/div/a')\

        # 遍历
        for big_node in big_node_list[:2]:
            big_name = big_node.xpath('./text()').extract_first()
            big_link = big_node.xpath('./@href').extract_first()

            # 获取小分类节点
            small_node_list = big_node.xpath('../following-sibling::ul/li[@name="cat_3"]/a')

            # 遍历
            for small_node in small_node_list[:2]:
                temp = {}
                temp['big_name'] = big_name
                temp['big_link'] = big_link
                temp['small_name'] = small_node.xpath('./text()').extract_first()
                temp['small_link'] = small_node.xpath('./@href').extract_first()
                # print(temp)

                # 模拟点击
                yield scrapy.Request(
                    url=temp['small_link'],
                    callback=self.parse_book_list,
                    meta={"py38": temp}
                )

    # 解析图书内容
    def parse_book_list (self, response):
         temp = response.meta['py38']
         book_link = response.xpath('//*[@id="component_59"]/li')

         for book in book_link[:2]:
             itme = DangdangItem()
             itme['big_name'] = temp['big_name']
             itme['big_link'] = temp['big_link']
             itme['small_name'] = temp['small_name']
             itme['small_link'] = temp['small_link']

             itme['name'] = book.xpath('./a/@title').extract_first()
             itme['book_link'] = book.xpath('./a/@href').extract_first()
             itme['author'] = book.xpath('./p[5]/span[1]/a/text()').extract_first()
             itme['Press'] = book.xpath('./p[5]/span[3]/a/text()').extract_first()
             itme['book_time'] = book.xpath('./p[5]/span[2]/text()').extract_first().strip()[1:]
             itme['price'] = book.xpath('./p[3]/span/text()').extract_first()
             itme['book_data'] = book.xpath('./p[2]/text()').extract_first()

             yield itme




