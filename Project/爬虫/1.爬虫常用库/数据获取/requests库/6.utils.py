# 使用request获取的response对象，具有cookies属性，该属性值是一个cookieJar类型，包含了对方服务器在本地的cookie。我们如何将其转换为cookie字典呢？
# 1.转换方法
# cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)
# 2.其中response.cookies返回的就是cookieJar类型的对象
# 3.requests.utils.dict_from_cookieJar函数返回cookies字典
import requests

url = 'http://www.baidu.com'

response = requests.get(url)
# <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
print(response.cookies)

dict_cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(dict_cookies)
jar_cookies = requests.utils.cookiejar_from_dict(dict_cookies)
# 丢失 了 域名 for .baidu.com
print(jar_cookies)  # <RequestsCookieJar[<Cookie BDORZ=27315 for />]>
