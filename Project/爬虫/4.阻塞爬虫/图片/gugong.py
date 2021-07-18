import requests
from lxml import etree
import os

def askurl(url,headers):
    resq = requests.get(url, headers=headers)
    data = resq.content.decode()
    html = etree.HTML(data)
    print(url)
    return html


def picture(html, headers, location):
    wallpaper_list = html.xpath('//*[@id="lights"]/div[2]/div/div[1]/a')
    n = 1
    for wallpaper in wallpaper_list:
        name = wallpaper.xpath('./img/@title')[0]
        likn = wallpaper.xpath('./img/@src')[0]
        if 'https://img.dpm.org.cn' not in likn:
            likn = 'https://img.dpm.org.cn' + likn
        if os.path.exists(location + '%s.jpg' % name):
            name = name + str(n)
            n += 1
        res = requests.get(likn, headers=headers).content
        with open(location + '%s.jpg' % name, "wb") as f:  # 以二进制形式保存图片
            f.write(res)


def pageget(html):
    page_url = html.xpath('//*[@id="next"]/@href')[0]
    url = 'https://www.dpm.org.cn' + page_url
    return url


if __name__ == '__main__':
    location = r'D:/图片/'
    if not os.path.exists(location):  # 首先判断是否存在当前文件夹如果没有则创建一个
        os.mkdir(location)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'}
    url = 'https://www.dpm.org.cn/lights/royal.html'
    while True:
        try:
            html = askurl(url, headers)
            picture(html, headers, location)
            url = pageget(html)
        except:
            break
