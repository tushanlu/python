import re
# re.compile函数
# 编译正则表达式，生成一个正则表达式（ Pattern ）对象
cop = re.compile(r'\d+')
Html = '12dd47a99b5c'

# re.match函数
# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
html = re.match(cop, Html).span()
print(html)

# re.search方法
# 扫描整个字符串并返回第一个成功的匹配
html = re.search(cop, Html).span()
print(html)

# re.findall
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
html = re.findall(cop, Html)
print(html)

# re.finditer
# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
html = re.finditer(cop, Html)
for i in html:
    print(i.group())

# re.split
# 按照能够匹配的子串将字符串分割后返回列表
html = re.split(cop, Html)
print(html)

# re.sub
# 用于替换字符串中的匹配项
html = re.sub('d', 'b', Html)
print(html)
