from selenium import webdriver


class Douyu(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start='
        self.opt = webdriver.ChromeOptions()
        self.opt.add_argument('--headless')
        self.opt.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=self.opt)

    def parseData(self, dataList):
        # 电影节点
        requ = self.driver.find_elements_by_xpath('*//div[@class="info"]')
        # 遍历，从每一个节点获取数据
        for dd in requ:
            dataDict = {}
            dataDict['标题'] = dd.find_element_by_xpath('./div/div[2]/div[1]/a').text
            dataDict['评分'] = dd.find_element_by_xpath('./div/div[2]/div[2]/div/span[2]').text
            dataDict['评价人数'] = dd.find_element_by_xpath('./div/div[2]/div[2]/div/span[4]').text
            try:
                dataDict['概识'] = dd.find_element_by_xpath('./div/div[2]/div[2]/p[2]').text
            except:
                dataDict['概识'] = '无'
            dataDict['详细链接'] = dd.find_element_by_xpath('./div/div[2]/div[1]/a').get_attribute('href')
            dataList.append(dataDict)
        return dataList

    def saveData(self, dataList):
        for data in dataList:
            print(data)


    def main(self):
        self.driver.get(self.url)
        dataList = []
        while True:
            datalist = self.parseData(dataList)
            self.saveData(datalist)
            self.driver.execute_script('scrollTo(0,document.body.scrollHeight)')
            try:
                next = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a')
                next.click()
            except:
                break
        print(len(datalist))
        self.driver.quit()


if __name__ == '__main__':
    douyu = Douyu()
    douyu.main()

