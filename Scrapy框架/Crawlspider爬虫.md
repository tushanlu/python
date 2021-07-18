## Crawlspider爬虫
+ 继承自 Spider  爬虫类

+ 自动根据规则提取链接并且发送给引擎

创建crawlspider爬虫
	scrapy genspider [-t crawl] name domains

```python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import DoubanItem


# CrawlSpider一般用于提取数据都在一个页面
class DoubanCrawlSpider(CrawlSpider):
    name = 'douban_crawl'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']
    # rules是一个元组
    rules = (   # 使用Rule类生成链接提取规则对象
        # 链接提取规则
        # follow参数决定是否在链接提取的链接对应的响应中继续应用链接提取器提取链接

        # LinkExtractor用于设置链接提取规则, 一般用allow参数,接受正则表达式
        # 设置详情叶面提取链接
        Rule(LinkExtractor(allow=r'subject/\d+/'), callback='parse_item'),
        # 翻页规则
        Rule(LinkExtractor(allow=r'\?start=\d+'), follow=True),
            )

    # 不能重写parse方法
    def parse_item(self, response):
        item = DoubanItem()
        item['name'] = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['score'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract_first()
        # print(response.url)

        yield item
```