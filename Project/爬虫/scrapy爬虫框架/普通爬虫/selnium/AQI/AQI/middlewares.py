# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import time
from scrapy.http import HtmlResponse


class SeleiumMiddleware(object):

    def process_request(self, request, spider):
        url = request.url

        if 'daydata' in url:
            opt = webdriver.ChromeOptions()
            # opt.add_argument('--headless')
            # opt.add_argument('--disable-gpu')
            driver = webdriver.Chrome(options=opt)
            driver.get(url)
            time.sleep(3)
            data = driver.page_source

            driver.close()
            # 创建响应对象
            res = HtmlResponse(url=url, body=data, encoding='utf-8', request=request)
            return res


