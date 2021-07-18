# 1.定位js文件
#   1.通过initiator定位到js文件
#   2.通过search 搜索关键字定位到js文件
#   3.通过元素绑定的事件监听函数找到js文件
#    三种方法不保证每一种都能找到，一起用
# 2.分析js代码,找到关键代码
# 3.模拟重现
#  1.通过第三方js加载模块直接加载js运行   js2py pyv8 execjs
#  2.纯python实现

# 通过第三方js加载模块直接加载js运行
import js2py
import requests
import json


def login():
    # 创建session对象
    session = requests.session()
    # headers
    session.headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36 Edg/84.0.522.63'}
    # 发送获取公钥数据包的请求
    response = session.get('http://activity.renren.com/livecell/rKey')
    # print(response.content)
    # 创建n
    n = json.loads(response.content.decode())['data']
    # print(n)
    # 创建t
    t = {'password': 'l071100.'}
    # 获取前置的js 代码
    rsaJs = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js').content.decode()
    bigintJs = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js').content.decode()
    barrettJs = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js').content.decode()

    # 创建js执行环境对象
    context = js2py.EvalJs()

    # 加载变量和js代码
    context.execute(rsaJs)
    context.execute(bigintJs)
    context.execute(barrettJs)
    context.n = n
    context.t = t

    # 将关键代码放环境中去
    pwdJs = '''
    t.password = t.password.split("").reverse().join(""),
    setMaxDigits(130);
    var o = new RSAKeyPair(n.e,"",n.n)
    , r = encryptedString(o, t.password)   
    '''
    context.execute(pwdJs)

    # 获取加密密码
    # print(context.r)

    # 构建formdata
    formData = {
        'phoneNum': '15807620838',
        'password': context.r,
        'c1': -100,
        'rKey': n['rkey']
                }
    # print(formData)D

    # 发送post请求，模拟登入
    response = session.post('http://activity.renren.com/livecell/ajax/clog', data=formData)

    # 验证
    print(response.content.decode())


if __name__ == '__main__':
    login()
