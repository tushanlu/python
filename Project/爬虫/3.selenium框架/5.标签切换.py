from selenium import webdriver
import time
driver = webdriver.Chrome()

url = 'https://wx.58.com/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT'

driver.get(url)

# 打印当前url
print(driver.current_url)
# 打印当前句柄
print(driver.window_handles)
time.sleep(3)
# 定位到租房
el = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a')
# 点击租房
el.click()

# 打印当前url
print(driver.current_url)
# 打印当前句柄
print(driver.window_handles)

# 选择最新打开的窗口句柄
driver.switch_to.window(driver.window_handles[-1])

el_list = driver.find_elements_by_xpath('/html/body/div[7]/div[2]/ul/li/div[2]/h2/a[1]')


for el in el_list:
    print(el.text, el.get_attribute('href'))
print(len(el_list))
time.sleep(5)
driver.quit()