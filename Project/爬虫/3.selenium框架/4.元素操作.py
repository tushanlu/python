from selenium import webdriver
import time
driver = webdriver.Chrome()

url = 'https://wx.58.com/chuzu/?utm_source=sem-sales-baidu-pc&spm=160476595549.22031703715&utm_campaign=sell&utm_medium=cpc&showpjs=pc_fg'

driver.get(url)

time.sleep(3)
el_list = driver.find_elements_by_xpath('/html/body/div[7]/div[2]/ul/li/div[2]/h2/a')

# with open('html.html', 'a', encoding='utf8') as f:
#     f.write(driver.page_source)
print(el_list)
for el in el_list:
    print(el.text, el.get_attribute('href'))

time.sleep(3)
driver.quit()
