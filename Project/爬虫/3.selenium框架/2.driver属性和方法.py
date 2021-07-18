# driver.page_source 当前标签页浏览器渲染之后的网页源代码
# driver.current_url 当前标签页的url
# driver.close() 关闭当前标签页，如果只有一个标签页则关闭整个浏览器
# driver.quit() 关闭浏览器
# driver.forward() 页面前进
# driver.back() 页面后退
# driver. save_screenshot() 页面截图

import time
from selenium import webdriver

url = 'http://www.baidu.com'

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 访问指定的url地址
driver.get(url)

# 显示源码
print(driver.page_source)
# 显示响应对应的url
print(driver.current_url)
print(driver.title)

time.sleep(2)

driver.get('https://www.douban.com')
time.sleep(2)
# 后退
driver.back()
time.sleep(2)
# 前进
driver.forward()

time.sleep(2)
# 保存网页快照，常用于验证是否运行或者验证码截图
driver.save_screenshot('douban.png')
# 关闭当前标签
driver.close()
# 关闭浏览器
driver.quit()
