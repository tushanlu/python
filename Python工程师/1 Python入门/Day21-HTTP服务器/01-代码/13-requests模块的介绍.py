# requests 模块是第三方的模块，可以用来发送网络连接
# pip install requests

import requests

response = requests.get('http://127.0.0.1:8090')
# print(response)  结果是一个Response对象

# content 指的是返回的结果，是一个二进制,可以用来传递图片
# print(response.content.decode('utf8'))  # 将二进制解码成为字符串

# 获取到的结果就是一个文本
print(response.text)

print(response.status_code)  # 200

# 如果返回的结果是一个 json 字符串，可以解析json字符串
# print(response.json())

r = requests.get('http://127.0.0.1:8090/test')
t = r.text  # 获取到 json 字符串
print(t, type(t))  # {"name": "zhangsan", "age": 18} <class 'str'>

j = r.json()  # 把 json 字符串解析成为python里对应的数据类型
print(j, type(j))  # {'name': 'zhangsan', 'age': 18} <class 'dict'>
