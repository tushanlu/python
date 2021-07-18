from selenium import webdriver


url = 'https://www.baidu.com/'

# 创建配置对象
opt = webdriver.ChromeOptions()
# 开启无界面模式
# 添加配置参数
# opt.add_argument('--headless')
# opt.add_argument('--disable-gpu')
# 使用代理
# 配置对象添加使用代理IP的命令
# 更换IP代理,必须重启浏览器
opt.add_argument('--proxy--server=http//:175.42.123.245:9999')
# 替换user-agent
# 配置对象添加替换user-agent的命令
opt.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Mobile Safari/537.36')

#  创建浏览器对象的时候添加配置对象

driver = webdriver.Chrome(options=opt)
driver.get(url)

driver.save_screenshot('baidu到此一游.png')











