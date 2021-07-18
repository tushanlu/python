from selenium import webdriver
import time
driver = webdriver.Chrome()

url = 'https://qzone.qq.com/'


driver.get(url)
driver.switch_to.frame('login_frame')

driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('483373342')
driver.find_element_by_id('p').send_keys('tulu0000')
driver.find_element_by_id('login_button').click()


time.sleep(5)
url = 'https://mail.163.com/'
driver.get(url)
el = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/div[4]/div[1]/div[1]/iframe')
driver.switch_to.frame(el)

driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input').send_keys('TLeuler')
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]').send_keys('TL071100')
driver.find_element_by_xpath('//*[@id="dologin"]').click()

time.sleep(5)
driver.quit()