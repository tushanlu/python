import hashlib
data = 'python38'
# 创建hashlid对象
md5 = hashlib.md5()

# 向hash对象中添加需要做hash运算的字符串

md5.update(data.encode())

# 获取字符串的hash值
result = md5.hexdigest()
print(result)
# 地址去重
#    url
#    url-hash
#    布隆过滤器
# 文本内容去重
#     编辑距离
#     simhash
