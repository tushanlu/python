from selenium import webdriver
import time


opt = webdriver.ChromeOptions()

opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=opt)

url = 'http://www.baidu.com'


driver.get(url)

# cookies = {data['name']: data['value'] for data in driver.get_cookies()}
cookies = driver.get_cookies()
print(cookies)

# 删除一条cookies

driver.delete_cookie('CookieName')

# 清空cookies
driver.delete_all_cookies()

time.sleep(5)
driver.quit()

