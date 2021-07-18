import requests

url = 'http://www.baidu.com'
# #发送带请求头的请求

head = {

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
            }
# 在请求头中带上User-Agent，模拟浏览器发送请求
response = requests.get(url, headers=head)
data = response.content.decode()
print(data)
# 打印请求头信息
print(response.request.headers)
