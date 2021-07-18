# find_element_by_id（返回一个元素）
# find_element（s）_by_class_name （根据类名获取元素列表）
# find_element（s）_by_name（根据标签的name属性值返回包含标签对象元素的标签）
# find_element（s）_by_xpath（返回一个包含元素的列表）
# find_element（s）_by_link_text（根据连接文本获取元素列表）
# find_element（s）_by_partial_link_text（根据链接包含的文本获取元素列表）
# find_element（s）_by_tag_name（根据标签名获取元素列表）
# find_element（s）_by_css_selector（根据css选择器来获取元素列表）
#  注意:
#     多了个s就返回列表，没有s就返回匹配到的第一个标签对象
#     find_element匹配不到就抛出异常，find_elements匹配不到就返回空列表
#     by_link_text和by_partial_link_text的区别：全部文本和包含某个文本

import time
from selenium import webdriver

driver = webdriver.Chrome()

url = 'http://www.baidu.com'
driver.get(url)

# 通过xpath进行元素定位
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
# 通过css选择器进行元素定位
# driver.find_element_by_css_selector('#kw').send_keys('java')
# 通过name属性值进行元素定位
# driver.find_element_by_name('wd').send_keys('html')
# 通过class属性值进行元素定位
# driver.find_element_by_class_name('s_ipt').send_keys('ruby')

# 通过链接文本进行元素定位
# driver.find_element_by_link_text('hao123').click()
# driver.find_element_by_partial_link_text('hao').click()

# 目标元素在当前html中是唯一标签的时候或者是众多定位出来的标签中的第一个的时候才能使用
print(driver.find_element_by_tag_name('title'))

driver.find_element_by_id('su').click()
time.sleep(3)
driver.quit()

