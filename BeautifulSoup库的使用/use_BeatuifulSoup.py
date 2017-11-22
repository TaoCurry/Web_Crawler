#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
1.Beautiful Soup是一个可以从HTML或XML文件中提取数据的Python库.它能够通过你喜欢的转换器/解析器(parser)实现惯用的文档导航、查找、修改文档的方式.
推荐使用lxml解析器,解析速度快，文档容错能力强 --> BeautifulSoup(markup, “lxml”)  markup可以是一个本地HTML文档或html字符串

2.Beautiful Soup3目前已经停止开发，推荐在现在的项目中使用Beautiful Soup4，不过它已经被移植到BS4了，也就是说导入时我们需要 import bs4 。

3.BeautifulSoup(open('index.html', 'lxml'))   # 传入本地的一个html文件

4.Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .

5. Tag:HTML开始标签+元素内容+结束标签 BeautifulSoup所查找的标签是第一个符合要求的标签，并不能返回所有满足要求的标签。
Tag有两个重要的属性:name attrs
name: soup 对象本身比较特殊，它的name即为[document] ; 其他内部标签，输出的值便为标签本身的名称
attrs: 返回一个字典，里面有标签所对应的所有属性-->CSS

6.NavigableString(可以遍历的字符串) 获取标签内部的文字   -------------------    须注意和Comment区别
soup.tag.string --> type(soup.tag.string) <class 'bs4.element.NavigableString'>

7. BeautifulSoup对象表示的是一个文档的全部内容大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性。
soup.name --> [document]
soup.attrs --> {}

8. Comment(文档中注释) [HTML注释结构:<!-- -->]      Comment对象是一个特殊类型的 NavigableString 对象，输出的内容会隐藏HTML中的注释符号.
type(soup.tag.string) <class 'bs4.element.Comment'>

9.遍历文档树
 文档树：HTML文档中的元素是分层次的，我们可以把这种层次归纳为几种关系：包含(嵌套、父子、继承)关系与并列(邻居、相邻、兄弟)关系.文档的层次也被称为文档树。

 .contents: Tag的 .contents 属性可以将Tag的子节点以列表(list)的方式输出; BeautifulSoup对象本身一定会包含子节点,也就是说<html>标签也是 BeautifulSoup对象的子节点.

 .children：Tag .children 属性生成一个list iterator object 可以进行迭代操作.
 soup.children --> <list_iterator object at 0x000002952625E5F8> list迭代器
  .contents属性和.children属性,仅包含Tag的直接子节点
 ---------------------------------------------------------------------------------------------------------------------------------

 .descendants: 返回Tag所有子孙节点,.descendants 属性可以对所有Tag的子孙节点进行递归循环.
 soup.descendants --> <generator object descendants at 0x0000021C3E338BF8> 生成器对象

 10.多个节点
 .strings: soup.strings --> <generator object _all_strings at 0x000001713CF78BF8> 生成器对象，迭代获取所有节点的内容.包含空行和空格

 .stripped_strings: soup.stripped_strings --> <generator object stripped_strings at 0x000001B654128BF8>生成器对象，迭代获取所有节点的内容.不包含空行或空格

 11.父节点： .parent属性获取某个元素的父节点.
 <html>的父节点是BeautifulSoup对象，type(soup.html.parent) --> <class 'bs4.BeautifulSoup'>
  BeautifulSoup.parent --> None

 12.兄弟节点： .next_sibling (下一个兄弟节点)&& .previous_sibling (前一个兄弟节点)

 13.搜索文档树：两个方法搜索文档树 find()  &&  find_all()
  BeautifulSoup.find() --> 获取第一个满足条件的内容
  BeautifulSoup.find_all(name, attrs, recursive, text,**kwargs) --> 列表(list)形式返回所有满足条件的对象，<class 'bs4.element.ResultSet'>，可以进行迭代  操作。如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回；如果传入True，可以匹配任何值。

 14.CSS选择器  通过 BeautifulSoup.select() 实现 返回的是一个列表(list)
 筛选原则是:标签名(tag)不加任何修饰，类名(.class)前加点，id(#id)名前加 #
"""
__author__ = "Curry"

from bs4 import BeautifulSoup

# 创建一个html文档
html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''


soup = BeautifulSoup(html_doc, 'lxml')
'''
print(soup.prettify())    # 格式化输出，以文档树的形式
print(soup.title)   # <title>The Dormouse's story</title>  tag title的所有内容
print(soup.title.name)   # title
print(soup.title.string)    # The Dormouse's story 网页真正展示的标题
print(soup.a)   # 获取第一个a标签
print(soup.find_all('a'))   # 找到所有a标签的内容，并将其以list形式返回,是一个可迭代对象Iterable.


# 从文档中找到所有<a>标签的链接
for link in soup.find_all('a'):
    print(link.get('href'))

# 从文档中获取所有文字内容：
print(soup.get_text())  # 会包括行数
'''
''''
print(soup.name)
print(soup.attrs)
print(soup.head.name)
print(soup.a.attrs)
print(soup.a['href'])
print(soup.a.string)
print(type(soup.a.string))
'''
# soup = BeautifulSoup(open('index.html'), 'lxml')   # 传入本地的一个html文件
'''
tag = soup.head
print(tag)    # <head><title>The Dormouse's story</title></head>
print(tag.contents)  # [<title>The Dormouse's story</title>]
print(soup.contents[0].name)    # html
'''
# print(soup.head.children)   # <list_iterator object at 0x000002952625E5F8> 迭代对象
'''
for child in soup.head.children:
    print(child)
# result: <title>The Dormouse's story</title>
for descend in soup.descendants:
    print(descend)
    
#print(soup.descendants)     # <generator object descendants at 0x0000021C3E338BF8>

#print(soup.prettify())
for string in soup.strings:
    print(string)

for strip_strings in soup.stripped_strings:
    print(strip_strings)

print(soup.get_text())
print('----------------')
for strip_strings in soup.stripped_strings:
    print(strip_strings)
print('----------------')
for strings in soup.strings:
    print(strings)

print(soup.title.parent)
print(type(soup.html.parent))
print(soup.find_all(['a', 'b']))

for tag in soup.find_all(True):
    print(tag.name)

'''
print(soup.select('title'))
print(soup.select('.title'))    # class="title"
print(soup.select('#link1'))    # id="link1"
print(soup.select('p #link2'))