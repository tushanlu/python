import scrapy


class Git2Spider(scrapy.Spider):
    name = 'git2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        token = response.xpath('//*[@id="login"]/form/input[1]/@value').extract_first()
        required_field = response.xpath('//*[@id="login"]/form/div[4]/input[6]/@name').extract_first()
        timestamp = response.xpath('//*[@id="login"]/form/div[4]/input[7]/@value').extract_first()
        timestamp_secret = response.xpath('//*[@id="login"]/form/div[4]/input[8]/@value').extract_first()

        post_data = {
            'commit': 'Sign in',
            'authenticity_token': token,
            'ga_id': '',  # ga_id类似固定值
            'login': 'moyanmowen',
            'password': 'tulu0000',
            'webauthn-support': 'supported',
            'webauthn-iuvpaa-support': 'unsupported',
            'return_to': '',
            required_field: '',
            'timestamp': timestamp,
            'timestamp_secret': timestamp_secret
        }

        # 针对登入url发送post请求
        yield scrapy.FormRequest(url='https://github.com/session',
                                 callback=self.after_login,
                                 formdata=post_data)

    def after_login(self, response):
        yield scrapy.Request(url='https://github.com//moyanmowen',
                             callback=self.check_login,)

    def check_login(self, response):
        print(response.xpath('/html/head/title/text()').extract_first())

