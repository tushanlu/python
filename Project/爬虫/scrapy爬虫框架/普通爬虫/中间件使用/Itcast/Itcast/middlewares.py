# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import random
from scrapy import signals
from Itcast.settings import USER_AGENT_LIST, PROXY_LIST
import base64


# 定义一个中间件类
class RamodmUSERAGENT(object):

    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = ua
        print(request.headers)


class RamodmProxy(object):

    def process_request(self, request, spider):
        proxy = random.choice(PROXY_LIST)
        # 如果需要账号认证
        if 'PSS' in proxy:
            # 对帐号加密
            bs64 = base64.b64decode(''.encode())
            # 认证
            request.headers['Proxy-Authorization'] = 'BaSiC ' + bs64.decode()
            # 设置代理
            request.meta['proxy'] = 'http://' + proxy['ip_port']
        else:
            # 设置代理
            request.meta['proxy'] = 'http://' + proxy['ip_port']
