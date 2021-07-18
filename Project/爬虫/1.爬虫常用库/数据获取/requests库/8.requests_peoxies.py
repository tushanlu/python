import requests


url = 'http://www.baidu.com'
proxies = {
    "http": "http://12.34.56.78:9000",
    "https": "https://12.34.56.78:9000"
}
try:
    response = requests.get(url, proxies=proxies, timeout=0.2)
    print(response.content.decode())
except :
    print('ip无效')
