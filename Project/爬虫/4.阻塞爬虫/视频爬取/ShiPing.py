import ffmpy3
import os
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as Threab


# 搜索

search_url = 'http://jisudhw.com/index.php'
search_keyword = input()
search_params = {'m': 'vod-search'}
search_headere = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
        }
search_datas = {
        'wd': search_keyword,
        'submit': 'search'
}
r = requests.post(search_url, params=search_params, data=search_datas)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')
soup = soup.find_all('span', class_='xing_vb4')

server = 'http://jisudhw.com'
for span in soup:
        url = server + span.a.get('href')
        name = span.a.string
        print(url)
        print(name)
        video_dir = name
        if name not in os.listdir('./'):
                os.mkdir(name)

        # 解析详情页面
        detail_url = url
        resp = requests.get(detail_url)
        resp.encoding = 'utf-8'
        detail_bf = BeautifulSoup(resp.text, 'lxml')
        num = 1
        search_res = {}
        for each_uel in detail_bf.find_all('input'):
                if 'm3u8' in each_uel.get('value'):
                        url = each_uel.get('value')
                        if url not in search_res.keys():
                                search_res[url] = num
                        print('第%d集' % num)
                        print(url)
                        num += 1


# 下载
def downvideo(url):
        num = search_res[url]
        name = os.path.join(video_dir, '第%d集.mp4' % num)
        ffmpy3.FFmpeg(inputs={url: None}, outputs={name: None}).run()


# 开启多线程下载
pool = Threab(8)
results = pool.map(downvideo, search_res.keys())
pool.close()
pool.join()
