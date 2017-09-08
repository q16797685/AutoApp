#!/usr/bin/python
# coding:utf-8

"""Created on 2017-06-29

@author: Wangchenyang

@功能：打印日志
"""

import time

logfile = open('E:/appLog/log.txt', 'a+')


def recordLog(text=0, tag_name=0):
    record_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    record_line = "%s      '%s'     '%s'\n" % (record_time, text, tag_name)
    logfile.write(record_line)
    logfile.flush()
