import scrapy
from scrapy_splash import SplashRequest


class SplashSpider(scrapy.Spider):
    name = 'splash'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/s?wd=110']

    def start_requests(self):
        yield SplashRequest(
            url=self.start_urls[0],
            callback=self.parse,
            args={'wait': 5},   # 最大超时时间
            endpoint='render.html'
        )

    def parse(self, response, **kwargs):
        with open('baidu.html', 'wb')as f:
            f.write(response.body)
