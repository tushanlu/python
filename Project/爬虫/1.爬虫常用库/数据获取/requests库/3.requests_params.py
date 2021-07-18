import requests

# #发送带参数的请求
# 在url中直接带参数
url = 'https://www.baidu.com/s?wd=python'
head = {

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
            }
response = requests.get(url, headers=head)
response.content.decode()


# 通过params携带参数字典
url = 'https://www.baidu.com/s?'
# 请求参数是一个字典
kw = {'wd': 'python'}
head = {

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
            }
# 带上请求参数发起请求，获取响应
response = requests.get(url, headers=head, params=kw)
print(response.content)
