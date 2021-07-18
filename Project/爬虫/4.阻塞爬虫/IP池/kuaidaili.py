import time
import parsel
import requests
import sqlite3
import asyncio
import random


def askurl(url):
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'}
    resq = requests.get(url, headers=head)
    return resq.content.decode()


def getdata():
    k, j = 1, 1
    datalist = []
    for i in range(0, 500):
        print('-------正在爬取第%03d页---------' % j)
        url = f'https://www.kuaidaili.com/free/inha/{k}/'
        data = askurl(url)
        soup = parsel.Selector(data)
        data_html = soup.xpath('//*[@class="table table-bordered table-striped"]/tbody/tr')
        for tr in data_html:
            ip = tr.xpath('./td[1]/text()').extract_first()
            ip_port = tr.xpath('./td[2]/text()').extract_first()
            html_dict = ip + ':' + ip_port
            datalist.append(html_dict)
        k += 1
        j += 1
        time.sleep(random.uniform(0.5, 2.0))
    print('获取到的IP数量', len(datalist))
    return datalist


async def check_ip(datalist):
    # 检测代理ip的质量
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
    }
    can_use = []
    for proxie in datalist:
        try:
            proxies = {"http": "http://"+proxie}
            requests.get('http://www.baidu.com', headers=head, proxies=proxies, timeout=0.1)
            can_use.append(proxie)
        except Exception as e:
            print(e)
    print(can_use)
    print('能用的代理ip的数量', len(can_use))
    return can_use


def init_db(dbpath):
    sql = '''create table pool(
    IP text
    )'''   # 创建数据表
    conn = sqlite3.connect(dbpath)  # 打开或创建数据库
    cursor = conn.cursor()      # 获取游标
    cursor.execute(sql)     # 执行sql语句
    conn.commit()       # 提交数据库操作
    conn.close()        # 关闭数据库连接


# 保存可用代理到数据库
def savedatadb(can_use, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in can_use:   # 添加数据到数据表
        cur.execute("insert into pool values('%s')" % (data))
        conn.commit()
    cur.close()
    conn.close()


def main():
    datalist = getdata()
    loop = asyncio.get_event_loop()
    can_use = loop.run_until_complete(check_ip(datalist))

    dbpath = 'IPpool.db'
    savedatadb(can_use, dbpath)


if __name__ == '__main__':
    main()
