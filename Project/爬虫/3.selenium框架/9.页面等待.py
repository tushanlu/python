# 强制等待
# time.slep()
# 隐式等待
# 显示等待（了解）
#  明确等待某一个元素

from selenium import webdriver
import time
driver = webdriver.Chrome()

# 隐式等待
url = 'https://www.baidu.com/'
# 设置位置之后的所有元素定位操作都有最大等待时间十秒，超过设置时间之后报错
driver.implicitly_wait(10)
driver.get(url)

driver.find_element_by_xpath('//*[@id="_lg_img"]')
time.sleep(5)
driver.quit()



