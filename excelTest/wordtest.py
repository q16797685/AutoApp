#!/usr/bin/python
#coding:utf-8

'''
Created on 2017-xx-xx

@author: Wangchenyang
'''

from time import sleep
import win32com.client

RANGE = range(3,8)

def word():
    app = 'word'
    openword = win32com.client.Dispatch ('%s.Application' %app)
    wd = openword.Documents.Add()
#    print wd
    openword.Visible = True
    sleep(2)
    # sh.Cells(1,1).Value = 'Python-to-%s Demo' %app
    # sleep(1)
    # for i in RANGE:
    #     sh.Cells(i,1).Value = 'Line %d' % i
    #     sleep(1)
    # sh.Cells(i+2,1).Value = "Th-th-th-that's all folks!"
    #
    # warn(app)
    # ss.Close(False)
    # xl.Application.Quit()

if __name__ == '__main__':
    word()