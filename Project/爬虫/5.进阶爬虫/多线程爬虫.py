import requests
import time
from lxml import etree
from threading import Thread
from functools import cmp_to_key


# 给输出结果排序
def sortRule(x, y):
    for i in x.keys():
        c1 = int(i)
    for i in y.keys():
        c2 = int(i)
    if c1 > c2:
        return 1
    elif c1 < c2:
        return -1
    else:
        return 0


# 计算时间的装饰器
def caltime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print("costtime: ", time.time() - start)

    return wrapper


# 获取页面
def getPage(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
        # 'Cookie': '__mta=141898381.1589978369143.1590927122695.1590927124319.9; uuid_n_v=v1; uuid=EDAA8A109A9611EABDA40952C053E9B506991609A05441F5AFBA3872BEA6088C; _csrf=f36a7050eb60429b197a902b4f1d66317db95bde0879648c8bff0e8237e937de; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1589978364; mojo-uuid=8b4dad0e1f472f08ffd3f3f67b75f2ab; _lxsdk_cuid=17232188c2f0-022085e6f29b1b-30657c06-13c680-17232188c30c8; _lxsdk=EDAA8A109A9611EABDA40952C053E9B506991609A05441F5AFBA3872BEA6088C; mojo-session-id={"id":"afcd899e03fe72ca70e34368fe483d15","time":1590927095603}; __mta=141898381.1589978369143.1590063115667.1590927111235.7; mojo-trace-id=10; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1590927124; _lxsdk_s=1726aa4fd86-ba9-904-221%7C%7C15',
    }
    try:
        resp = requests.get(url=url, headers=headers)
        if resp.status_code == 200:
            return resp.text
        return None
    except Exception as e:
        print(e)
        return None


# 获取单个页面数据
def parsePage(page):
    if not page:
        yield
    data = etree.HTML(page).xpath('.//dl/dd')
    for d in data:
        rank = d.xpath("./i/text()")[0]
        title = d.xpath(".//p[@class='name']/a/text()")[0]
        yield {
            rank: title
        }


# 调度
def schedule(url, f):
    page = getPage(url)
    for data in parsePage(page):
        f.append(data)


# 数据展示
def show(f):
    f.sort(key=cmp_to_key(sortRule))
    for x in f:
        print(x)


@caltime
def main():
    urls = ['https://maoyan.com/board/4?offset={offset}'.format(offset=i) for i in range(0, 100, 10)]
    threads = []
    f = []
    for url in urls:
        # schedule(url, f)
        t = Thread(target=schedule, args=(url, f))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    show(f)


if __name__ == '__main__':
    while True:
        main()
