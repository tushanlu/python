import requests
import json
from jsonpath import jsonpath
url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'}

response = requests.get(url, headers=headers)

dict_data = json.loads(response.content)
# 打印出所有A开头的城市
print(jsonpath(dict_data, '$..A..name'))
# 打印出所有T开头的城市
print(jsonpath(dict_data, '$..T..name'))
# 打印出所有城市
print(jsonpath(dict_data, '$..name'))

