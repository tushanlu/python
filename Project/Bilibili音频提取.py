import requests
import json
import os
import sys
import asyncio
import aiohttp
import re
from lxml import etree
from time import time


async def getData(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def schedule(url, datalist):
    for html in audio_link(await getData(url)):
        datalist.append(html)


def audio_link(data):
    # 定位到script
    html = etree.HTML(data)  # 创建element对象
    scripts = html.xpath("/html/head/script[5]/text()")[0]
    script = scripts.split("window.__playinfo__=")[1]
    script_json = json.loads(script)
    # 获取标题
    title = html.xpath('//*[@id="viewbox_report"]/h1/@title')[0]
    # 去除标点符号
    re.sub(r'\W', ' ', title)
    # 解析音频的地址
    audio_url = script_json["data"]['dash']["audio"][0]["baseUrl"]
    print(audio_url)
    yield {"audio_url": audio_url, "title": title}


def download(audio_url, title, headers):
    if os.path.exists(location+"%s.mp3" % title):
        print("文件已存在")
        return
    if "logo=80000000" in audio_url:
        audiocontent = session.get(audio_url, headers=headers).content
    else:
        audiocontent = requests.get(audio_url).content
    print(audiocontent)
    with open(location + '%s.mp3' % title, 'wb') as f:
        f.write(audiocontent)
        f.close()


def main():
    try:
        datalist = []
        threads = []
        url = input("输入链接(多链接时，以英文逗号隔开):")
        # 判断网址是否正确
        if not re.fullmatch(r'https?:/{2}w{3}\.(bili){2}\.com.*', url):
            print("url错误")
            return
        link = url.split(',')
        loop = asyncio.get_event_loop()
        for url in link:
            threads.append(schedule(url, datalist))
        loop.run_until_complete(asyncio.wait(threads))
        for i, bili in enumerate(datalist):
            print("任务：{}/{}".format(i+1, len(datalist)))
            download(bili["audio_url"], bili["title"], headers)
            print("{}下载完成".format(bili["title"]))
        num = input("输入0退出,回车继续>")
        if num == "0":
            loop.stop()
            loop.close()
            sys.exit()
    except requests.exceptions.MissingSchema:
        print("出现bug，系统错误，请自行解决")
        sys.exit()


if __name__ == '__main__':

    print("-----Bililili音频提取-----")
    # location = "./Bilibili_audio/"
    location = input("输入保存路径(格式：D:/xxx/):")

    session = requests.session()
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "dnt": "1",
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"
    }
    # 判断文件夹是否存在
    if not os.path.exists(location):
        os.mkdir(location)
    while True:
        main()
