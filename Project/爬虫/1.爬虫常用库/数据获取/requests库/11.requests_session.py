# 利用requests.session进行状态保持

# requests模块中的Session类能够自动处理发送请求获取响应过程中产生的cookie，进而达到状态保持的目的。

# requests.session的作用及应用场景

# requests.session的作用
# 自动处理cookie，即下一次请求会带上前一次的cookie
# requests.session的应用场景
# 自动处理连续的多次请求过程中产生的cookie

# requests.session使用方法

# session实例在请求了一个网站后，对方服务器设置在本地的cookie会保存在session中，下一次再使用session请求对方服务器的时候，会带上前一次的cookie
# session = requests.session()  # 实例化session对象
# response = session.get(url, headers, ...)
# response = session.post(url, data, ...)

# 案例-github模拟登录
import requests
import re


def login():
    # session
    session = requests.session()
    # headers
    session.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.61'}
    # url1-获取token
    url1 = 'https://github.com/login'
    # 发送请求获取响应
    res1 = session.get(url1).content.decode()
    # 正则提取
    token = re.findall('name="authenticity_token" value="(.*?)" />', res1)[0]
    required_field = re.findall('type="text" name="(.*?)"', res1)[1]
    timestamp = re.findall('name="timestamp" value="(.*?)"', res1)[0]
    timestamp_secret = re.findall('name="timestamp_secret" value="(.*?)" />', res1)[0]
    # print(token)
    # print(required_field)
    # print(timestamp)
    # print(timestamp_secret)

    # url2-登录
    url2 = 'https://github.com/session'
    # 构建表单数据
    data = {
        'commit': 'Sign in',
        'authenticity_token': token,
        'ga_id': '',     # ga_id类似固定值
        'login': 'moyanmowen',
        'password': 'tulu0000',
        'webauthn-support': 'supported',
        'webauthn-iuvpaa-support': 'unsupported',
        'return_to': '',
        required_field: '',
        'timestamp': timestamp,
        'timestamp_secret': timestamp_secret
    }

    # 发送请求登录
    session.post(url2, data=data, verify=False, timeout=10)

    # url3-验证
    url3 = 'https://github.com/moyanmowen'
    response = session.get(url3, timeout=20).content.decode()
    title = re.findall('<title>(.*?)</title>', response)
    # 验证正确，title中不含有 "·github"
    print(title)


if __name__ == '__main__':
    login()
