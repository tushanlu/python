import requests

url = 'http://www.baidu.com'

response = requests.get(url)
# print(response.encoding)
# 手动设定编码格式
response.encoding = 'utf-8'


# 打印源码的str类型数据
# print(response.text)
# print(response.encoding)


# response.content是存储的bytes类型的响应源码，可以进行decode操作
# print(response.content.decode())

# 解决中文乱码 ，利用response.content进行decode()

# 常见的编码字符集
# utf-8
# gbk
# gb2312
# ascii
# iso-8859-1


# 常见的响应对象参数和方法
# 响应url
print(response.url)

# 查看状态码
print(response.status_code)

# 响应对应的请求头
print(response.request.headers)

# 响应头
print(response.headers)

# 答应响应设置cookies
print(response.cookies)
