from selenium import webdriver
import time
driver = webdriver.Chrome()


url = 'https://jn.lianjia.com/'

driver.get(url)

# 滚动条拖动
# scrollTo(x,y)
# x水平移动，y垂直移动
# 滚动到最底部
# scrollTo(0,document.body.scrollHeight)
js = 'scrollTo(0,400)'
# 执行js语句
driver.execute_script(js)

driver.find_element_by_xpath('/html/body/div[20]/div[4]').click()
driver.find_element_by_xpath('/html/body/div[2]/ul/li/a/b').click()
time.sleep(5)
driver.quit()
