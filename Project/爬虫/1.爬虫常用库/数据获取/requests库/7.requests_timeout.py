# 1. 超时参数timeout的使用方法
# response = requests.get(url, timeout=3)
# 2. timeout=3表示：发送请求后，3秒钟返回响应，否则就会抛出异常


import requests

try:
    url = 'https://twitter.com/'
    response = requests.get(url, timeout=1)  # 设置超时时间
except:
    print('超时')
