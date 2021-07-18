# 如果该网站的CA证书没有经过【受信任的根证书颁发机构】的认证,直接访问会抛出包含ssl.CetifacateError...的异常
# 为了在代码中能够正常的请求，我们使用verify=False参数，此时requests模块发送请求时将不做CA证书的验证：verify参数能够忽略CA证书的认证
import requests
url = 'https://sam.huat.edu.cn:8443/selfservice/'

response = requests.get(url, verify=False)

