#!/usr/bin/python
# coding:utf-8

'''
Created on 2017-7-13

@author: wcy

@李教授精神科首诊流程
'''

import AutoTest.AppAutoTest.commonMethod as commonMethod
import AutoTest.AppAutoTest.answerQuestionnaire as answerQuestionnaire
import AutoTest.AppAutoTest.scale_SAS as scale_SAS
import AutoTest.AppAutoTest.scale_SDS as scale_SDS
import AutoTest.AppAutoTest.scale_SCL as scale_SCL

class Testclass(object):
    @classmethod
    def testcase(self):
        commonMethod.openApp(self)
        commonMethod.clickConfirm(self)
        commonMethod.chooseGhlb(self)
        commonMethod.chooseFirst(self)
        commonMethod.clickConfirm(self)
        commonMethod.clickZnwz(self)
        commonMethod.clickConfirm(self)
        answerQuestionnaire.questinNaire(self)
        print '问卷'
        """ 进入量表列表,选择SAS"""
        commonMethod.chooseScale_SAS(self)
        commonMethod.clickConfirm(self)
        scale_SAS.answerScalc_SAS(self)
        """ 进入量表列表,选择SDS"""
        commonMethod.chooseScale_SDS(self)
        commonMethod.clickConfirm(self)
        scale_SDS.answerScalc_SDS(self)
        """ 进入量表列表,选择SCL"""
        commonMethod.chooseScale_SCL(self)
        commonMethod.clickConfirm(self)
        scale_SCL.answerScalc_SCL(self)
        print 'yes'
        self.driver.quit()

if __name__ == '__main__':
    Test = Testclass(debug=True)
    Test.testcase()
