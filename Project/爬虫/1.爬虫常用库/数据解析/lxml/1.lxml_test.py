from lxml import etree

text = '''
    <div>
            <ul>
                <li class="item-1">
                    <a href="link1.html"> first item</a>		
                </li>
                <li class="item-1">
                    <a href="link2.html"> second item</a>		
                </li>
                <li class="item-inactive">
                    <a href="link3.html"> third item</a>		
                </li>
                <li class="item-1">
                    <a href="link4.html"> fourth item</a>		
                </li>
                <li class="item-0">
                    <a href="link5.html"> fifth item</a>		
                </li>
            </ul>
    </div>
'''

# 创建element对象
html = etree.HTML(text)
shtml = etree.tostring(html)
print(shtml)
# etree.HTML(html)会自动补全缺失的标签
print(html)
# 打印element对象有哪些方法
print(dir(html))

print(html.xpath('//a[@href="link1.html"]/text()'))
print(html.xpath('//a[@href="link1.html"]/text()')[0])

# [' first item', ' second item', ' third item', ' fourth item', ' fifth item']
text_list = html.xpath('//a/text()')
# ['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
link_list = html.xpath('//a/@href')
print(text_list)
print(link_list)

for text in text_list:
    myindex = text_list.index(text)
    link = link_list[myindex]
    print(text, link)

for text, link in zip(text_list, link_list):
    print(text, link)

el_list = html.xpath('//a')
for el in el_list:

    print(el.xpath('./text()'))
    print(el.xpath('./@href'))

