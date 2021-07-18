import scrapy


# scrapy模拟登陆-cookies参数使用
class Git1Spider(scrapy.Spider):
    name = 'git1'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com//moyanmowen']

    def start_requests(self):
        url = self.start_urls[0]

        temp = '_octo=GH1.1.572897933.1599022442; tz=Asia%2FShanghai; _device_id=ea885c662ebb03cba7285d2a82894a5c; has_recent_activity=1; user_session=GK92K0_4z4cbYyot6YjxmQrd0LCJaLs9zxCqe1L92B_0rEgU; __Host-user_session_same_site=GK92K0_4z4cbYyot6YjxmQrd0LCJaLs9zxCqe1L92B_0rEgU; tz=Asia%2FShanghai; logged_in=yes; dotcom_user=moyanmowen; _gh_sess=pb18liy5h6Eje59eySg9EzG90eRaVgn%2FhVN2xMe%2BUf3IzgehHu5qxCSAaX1EcavRVH5erWAqCoCpCFzjzmRKq3KxOXkxhW9F8GLJwAwyzJkTS8bTFLzBNlMrVvKAzXTtMWyRmWTACtF%2FMwrbFHsdK1GdCP32OvaRrjdaMlrnplOwpwAUgDOL74MV%2BSrlYmahtfsAfNj5VHypbSgafRAI8zaFooNu1kffWs6HRnXrpjERMhSoSspSmc7lnCTENj4m0suui1pype9mjZgcUkpVNAIq%2Br6KvbuSpWgcuLZCxK7bLZo0yyWSDyV788GECNsmbdgcRDkvhNph2QuC0NLser8shdQ2vK4xAx%2F7AZ06Zmls34wW2DwVU2sUDLVqSIC2XrsVSB2MfcynWg3OfLTiF6%2BUbilw4%2B8QnTxNPWU67iMMmI5n5tKKZXnBtpknK79uxGricofvCnnKUXMKwrOi5cna4aEcVlMUmM3s%2B5%2FvMztBFb2ogtFYx10latDb5aVRlZKT87puQGfOSPpuxyL10XTrU%2Bezh59X7CAttKxExyAoCjsG9GLOzdckrfc7zDbp8UpKtr5%2BG52a0tcdejsywSrJl%2FzDPTIOryg8Nu3Bk%2BGZvBiJAlpHivrPxoh3VHzdAQ6bV75iM18ic2c1wxIHTYKU3DSswORProJ9%2BP%2Bz9NSoNurb7gy7Jg%3D%3D--7y9ATmstBUIVEJnL--Bulxy8wadylTaDPS2xBTuw%3D%3D'
        cookies = {data.split('=')[0]: data.split('=')[-1] for data in temp.split(';')}
        yield scrapy.Request(url=url, cookies=cookies)

    def parse(self, response):
        print(response.xpath('/html/head/title/text()').extract_first())
