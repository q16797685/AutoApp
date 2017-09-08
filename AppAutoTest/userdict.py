#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-06-28

@author: Wangchenyang

@userdict:用户数据
"""

# 13307489560 涛哥
# 13307310742 唐志峰
# 15071001668 黄鹤

import mysql.connector
import random

num = [0, 1, 2]

__choicenumber = random.choice(num)

# conn=mysql.connector.connect(host='172.17.200.94',user='root',passwd='123456',db='FEMR',port=3306)
# cur = conn.cursor()
# cur.execute('select gender,telephone from PT_PATIENT where telephone in (13787044789,13307310742,15071001668);')
# results = cur.fetchall()

userdict = {'phone': ['13787044789', 0]}      # 0：代表男   1：代表女
phnumber = userdict['phone'][0]
gender = userdict['phone'][1]

# phnumber = results[__choicenumber][1]
# gender = results[__choicenumber][0]
