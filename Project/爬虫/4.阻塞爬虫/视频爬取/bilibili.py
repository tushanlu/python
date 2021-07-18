import you_get
import sys

from lxml import etree
import requests
from random import uniform


def getdata(baseurl):
    datalist = []   # 保存视频的信息
    daralink = []   # 保存下载链接
    n = 1
    k = 1
    for i in range(0, 20):  # 获取全部页面信息
        print('---正在爬取第%d页' % n)
        url = baseurl + str(n)
        data = askurl(url)
        soup = etree.HTML(data)        # 保存获取到的网页源码
        if n == 1:
            data_html = soup.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li')
        else:
            data_html = soup.xpath('//*[@id="all-list"]/div[1]/ul/li')
        for li in data_html:
            html_dict = {}
            name = li.xpath('./div/div[1]/a/@title')[0]    # 视频的名字
            link = "https:" + str(li.xpath('./a/@href|./div[2]/div[1]/a[1]/@href')[0])        # 视频详细的链接
            # 保存数据
            daralink.append(link)   # 添加链接
            html_dict[name] = link
            datalist[len(datalist):] = [k, html_dict]   # 添加视频的信息
            k += 1
        n += 1

    for datalist in datalist:
        print(datalist)
    return daralink


# 得到指定一个URL的网页
def askurl(url):
    head = {        # 模拟浏览器访问
        'Referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
    }
    resq = requests.get(url, headers=head, timeout=0.5)
    return resq.content.decode()


def download(url, t):
    # 视频输出的位置
    path = r'D:\Bilibili'
    qualitys = ['--format=dash-flv', '--format=flv720', '--format=flv480', '--format=flv360']
    quality = qualitys[t]
    try:
        sys.argv = ['you-get', '-o', path, quality, '-l', url]
        you_get.main()
    except:
        print('不支持的画质')


if __name__ == '__main__':
    blid = input('>搜索名称:')
    baseurl = f'https://search.bilibili.com/all?keyword={blid}&from_source=banner_search&page='
    daralink = getdata(baseurl)
    L = int(input('>输入下载视频的序号:')) - 1
    url = daralink[L]
    t = int(input('''   
>选择支持的画质
1:1008p
2: 720P
3: 480p
4:360p
''')) - 1
    download(url, t)
