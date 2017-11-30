#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
使用MongoDB
1、连接MongoDB,创建一个客户端 client = pymongo.MongoClient(host='xxx', port='xxx') 第一个参数为地址host,可以为本地也可以为网络客户端;第二个参数为端口port,默认27017.
2、创建数据库 database = client['XXX'] 创建一个名为XXX的数据库
3、在创建的数据库中创建一个表, collection = database['XXX'] 在刚刚创建的XXX创建了一个名为'XXX'的表
4、往表中插入数据 collection.insert_one()插入单条数据 && collection.insert_many([xxx, yyy, zzz])插入多条数据<传入一个列表参数>
  插入数据的过程中，每条数据都有一个_id属性来唯一标识，insert()方法会在执行后返回的_id值。
5、查询数据 collection.find_one({'xx': 'yy'}) 查询单个结果，返回一个字典类型  && collection.find() 查询多条数据。

 find()方法还可以指定查询条件 $lt/$lte/$gt/$gte/$ne 代表< 、 <= 、 > 、 >= 、！=
"""
__author__ = "Curry"

import pymongo

client = pymongo.MongoClient('localhost', 27017)    # 创建客户端 localhost表示为本地客户端，27017为端口号
database = client['Curry']   # 数据库的名称list[]中的内容
sheet_lines = database['sheet_lines']   # 在数据库中创建一个表单


with open(r'C:\Users\xiatao\Desktop\Test.txt', 'r') as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        data = {
            'index': index,
            'line': line,
            'word': len(line.split('\n'))
        }
        sheet_lines.insert_one(data)    # 将数据添加到数据库中


#for item in sheet_lines.find({'index': {'$lt': 200}}):
#    print(item['index'])  --> 0 1 2 ... 199
for item in sheet_lines.find():    # 检查数据是否导入数据中 mongodb的find()方法
    print(item)    # item类似字典类型 example --> {'_id': ObjectId('5a1ed06f3a468a84b1ec5ed3'), 'index': 0, 'line': 'aWQ6MTAwMC9nb29kczo1MDA=\n', 'word': 1}

