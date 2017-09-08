#!/usr/bin/python
#coding:utf-8

'''
Created on 2017-6-14

@author: wcy
'''


import  urllib2
import  urllib
import json

url = 'https://api.emr.fulcruminfo.cn/v1/users/login'
# data = {'mobile':'13787044789',
#         'password':'123',
#         'devicetype':'',
#         'devicesystem':'',
#         'deviceid':''}

data = {"deviceid":"1d1904010431c695","devicesystem":"Nexus 6P","devicetype":"android","mobile":"13646031510","password":"123456"}
#data = urllib.urlencode(data)
send_headers = {
 'Content-Type':'application/json',
}
req = urllib2.Request(url,urllib.urlencode(data),headers=send_headers)
response = urllib2.urlopen(req)
the_page = response.read()
text = json.loads(the_page)
print text