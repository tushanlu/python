# 路径查找
# / 依次查找
# // 间接查找
# ./ 从当前元素下查找
# .// 从当前元素的间接子节点下查找


# 位置条件
# //li[1] 整个文档中的第一个<li>标签
# //li[last()] 最后一个
# //li[position() < 3] 前2个
# //li[position() - 2] 倒数第二个


# 属性条件
# //li[@id="xxxx"]
# //li[@class="xxx"] @class属性名
# //li[@class="xx" and name="xxx"] 多个属性的且的关系


# 同时提取两个元素
# //title/text() | //img/@src


# 模糊条件
# //div[contains(@class, "page")] 查找class属性值包含page的所有div标签
# //div[starts-with(@class, "box")] 第一个class的属性值为box的div标签
# //div[ends-with(@class, "clearfix")] 最后一个class的属性值为clearfix的div标签
