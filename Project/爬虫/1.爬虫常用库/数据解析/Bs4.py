from bs4 import BeautifulSoup
import re

file = open('./baibu.html', 'rb')
html = file.read()
bs = BeautifulSoup(html, 'html.parser')
# 1.Tag     标签及其内容：第一个内容
dot = bs.head
# print(dot )

# 2.NavigadleString     标签里的内容（字符串）
dot = bs.title.string
# print(bs)

# 3.获得标签里的所有内容
dot = bs.a.attrs
# print(dot)


# ------------

# 文档的遍历
dot = bs.head.contents   # .contents 和.children 属性仅包含tag的直接子节点.更多搜索遍历文档树
# print(dot)

for dot in bs.descendants:  # descendants 属性可以对所有tag的子孙节点进行递归循环(先序遍历)
    print()
    # print(dot)
# 更多搜索遍历文档树

# 文档的搜索

# 1.find_all()
t_list = bs.find_all('a')   # 字符串过滤：会查找完全匹配的内容
# print(t_list)

# 正则表达式搜索:
t_list = bs.find_all(re.compile('a'))
# print(t_list)

# 方法；


def name_is(tag):
    return tag.has_attr('name')


t_list = bs.find_all(name_is)
# print(t_list)

# 2.kwargs  参数:
t_list = bs.find_all(id='head')
# print(t_list)

t_list = bs.find_all(class_=True)
# print(t_list)

# 3.text参数：
t_list = bs.find_all(text=['新闻', 'hao123', '地图', '视频', '贴吧'])
# print(t_list)

t_list = bs.find_all(text=re.compile(r'\d'))    # 查找包含特定文本的内容
# print(t_list)

# 4.limit 参数：限定个数
t_list = bs.find_all('a', limit=3)
# print(t_list)

# css选择器：
t_list = bs.select('title')     # 标签查找
# print(t_list)

t_list = bs.select('.mnav')     # 类名查找
# print(t_list)

t_list = bs.select('#u1')       # id查找
# print(t_list)

t_list = bs.select("a[class='bri']")        # 属性查找
# print(t_list)

t_list = bs.select('head > title')       # 子标签查找
# print(t_list)

t_list = bs.select('.mnav ~ .bri')      # 兄弟标签查找
# print(t_list)
