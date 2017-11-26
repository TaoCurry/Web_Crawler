#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
1. requests库的方法(HTTP协议的知识点)：
  <1>.requests.get(url, params, kwargs)    使用get方法获取url请求,对于带参数的url,传入一个dict作为params参数
  <2>.requests.post()    请求获取URL位置资源的响应消息报告，即获得该资源的头部信息
  <3>.requests.delete()    请求删除URL位置储存的资源
  <4>.requests.head()
  <5>.requests.put()    请求向URL位置储存一个资源，覆盖原URL位置的资源
  <6>.requests.patch()
2. requests库对象的属性
  <1>.requests.get.status_code()   HTTP响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误.
  <2>.requests.get.text()    HTTP响应内容的字符串形式，既url对应的页面内容 HTML编码内容
  <3>.requests.get.encoding   网页编码方式
  <4>.requests.get.content    二进制字节形式返回网页编码方式 b'xxx'  会自动解码 gzip 和 deflate 压缩
  <5>.requests.get.headers    以字典对象存储服务器响应头(Response Headers)，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
  <6>.requests.get.json
  <7>.requests.raise_for_status(self)    失败请求(非200响应)抛出异常
  <8>.requests.apparent_encoding    从内容中分析出的相应内容编码方式（备选编码方式）
"""

__author__ = "Curry"

import requests


print(r.status_code)    # HTTP请求的返回状态，200表示连接成功，404表示连接失败
print(r.text)
r = requests.get('https://www.baidu.com/s', params={'f': 8, 'rsv_bp': 1, 'rsv_idx': 1, 'word': '新浪微博', 'tn': '96885894_hao_pg'})
print(r.url)    # https://www.baidu.com/s?f=8&rsv_bp=1&rsv_idx=1&word=%E6%96%B0%E6%B5%AA%E5%BE%AE%E5%8D%9A&tn=96885894_hao_pg
print(r.status_code)
print(r.text)
print(r.encoding)
print(r.content)
print(r.apparent_encoding)



def getHTMLtext(url):   # 爬取网页的通用代码框架
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()    # 如果状态不是200，则引发异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬虫失败！')


if __name__ == '__main__':
    url = 'https://nba.hupu.com/'
    getHTMLtext(url)
