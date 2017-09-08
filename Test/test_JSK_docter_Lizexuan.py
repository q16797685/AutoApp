#!/usr/bin/python
# coding:utf-8

'''
Created on 2017-7-13

@author: wcy

@李则宣教授精神科首诊流程
'''

import AutoTest.AppAutoTest.commonMethod as commonMethod
import AutoTest.AppAutoTest.scale_SCL as scale_SCL
import AutoTest.AppAutoTest.Chief_Complaint as Chief_Complaint
import AutoTest.AppAutoTest.History_of_present_illness as History_of_present_illness
import AutoTest.AppAutoTest.Past_history as Past_history
import AutoTest.AppAutoTest.Personal_history as Personal_history
import AutoTest.AppAutoTest.Family_history as Family_history
import AutoTest.AppAutoTest.Marital_history as Marital_history


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
        Chief_Complaint.answerChief_Complaint(self)
        """ 完成主诉 """
        History_of_present_illness.answerHistory_of_present_illness(self)
        """ 完成现病史 """
        Past_history.answerPast_history(self)
        """ 完成既往史 """
        Personal_history.answerPersonal_history(self)
        """ 完成个人史 """
        Family_history.answerFamily_history(self)
        """ 完成家庭史 """
        Marital_history.answerMarital_history(self)
        """ 完成婚姻史 """
        """ 进入量表列表,选择SCL"""
        commonMethod.chooseScale_SCL(self)
        commonMethod.clickConfirm(self)
        scale_SCL.answerScalc_SCL(self)

if __name__ == '__main__':
    Test = Testclass()
    Test.testcase()
