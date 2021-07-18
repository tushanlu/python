# scrapyd部署scraoy项目

## scrapy的介绍
scrapyd是一个用于部署和运行scrapy爬虫的程序，它允许你通过JSON API来部署爬虫项目和控制爬虫运行，scrapyd是一个守护进程，监听爬虫的运行和请求，然后启动进程来执行它们
+ 所谓json api本质就是post请求的webapi

## scrapyd的安装
+ scrapyd服务：pip install scrapyd
+ scrapyd客户端：pip install scrapyd-client

## 启动scrapy服务
1. **在scrapy项目路径下启动scrapyd的命令 **：sudo scrapyd 或scrapyd
2. 启动之后就可以打开本地运行的scrapyd，浏览器中访问本地6800端口可以查看scrapyd的监控界面
![](.\图片\屏幕截图 2020-09-20 092044.png)


## scrapy项目部署
1. **配置需要部署的项目**
编辑需要部署的项目的scrapu.cfg文件（需要将哪一个爬虫部署到scrapy中，就配置该项目的该文件）
+ [deploy:部署名（可以自定义）]
+ url = http://localhost:6800/
+ project = 项目名

2. **部署项目到scrapyd**
同样在scrapy项目路径下执行
+ scrapyd-deploy 部署名 -p 项目名(win10要在python的Scripts目录下增加scrapyd-deploy.bat文件）
@echo off
"x:\xxxx\xxxx\python.exe" "x:\xxxx\xxxx\Scripts\scrapyd-deploy" %1 %2 %3 %4 %5 %6 %7 %8 %9
+ bat文件里是python.exe和scrapyd-deploy的绝对路径

3. **管理scraoy项目**
+ 启动项目：curl http://localhost:6800/schedule.json -d project=project_name -d spider=spider_name
+ 关闭爬虫：curl http://localhost:6800/cancel.json -d project=project_name -d job=jobid
+ **注意：curl是命令行工具，如果没有这需要安装**

4. **使用requests模块控制scrapy项目**
+ 