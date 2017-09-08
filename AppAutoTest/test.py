#!/usr/bin/python
#coding:utf-8

'''
Created on 2017-6-2

@author: wcy
'''

import commonMethod
import Chief_Complaint
import History_of_present_illness
import Past_history
import Personal_history
import Family_history
import Marital_history

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
        History_of_present_illness.answerHistory_of_present_illness(self)
        Past_history.answerPast_history(self)
        Personal_history.answerPersonal_history(self)
        Family_history.answerFamily_history(self)
        Marital_history.answerMarital_history(self)
        self.driver.quit()

if __name__ == '__main__':
    Test = Testclass()
    Test.testcase()
