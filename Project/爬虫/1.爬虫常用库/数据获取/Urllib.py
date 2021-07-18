import urllib.request
import urllib.parse
# 获得一个get请求
response = urllib.request.urlopen('http://www.baidu.com')
dec = response.read().decode('utf-8')    # 对获取到的网页源码进行utf-8解码
# print(dec)

# 获取post请求
data = bytes(urllib.parse.urlencode({}), encoding='utf-8')
response = urllib.request.urlopen('http://www.baidu.com', data=data)
dec = response.read().decode('utf-8')
# print(dec)

# 超时处理
try:
    response = urllib.request.urlopen('http://www.baidu.com', timeout=0.1)
    dec = response.read().decode('utf-8')  # 对获取到的网页源码进行utf-8解码
    # print(dec)
except urllib.error.URLError as t:
    print('超时')

# 获取信息
response = urllib.request.urlopen('http://www.baidu.com')
infs = response.getheaders()        # 获取全部信息
inf = response.getheader('Server')      # 获取单个信息
# print(infs)

# 模拟浏览器访问
url = 'https://movie.douban.com/top250?start='
head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
            }
request = urllib.request.Request(url, headers=head)

response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
# print(html)
