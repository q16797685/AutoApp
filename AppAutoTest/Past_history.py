#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-07-17

@author: Wangchenyang

@回答既往史
"""

from time import sleep


def answerPast_history(self):
    # 既往史
    # 获取第32题，多选
    answer_thirty_two = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    # log.recordLog(answer_thirty_two.text,answer_thirty_two.tag_name)
    answer_thirty_two.click()
    sleep(3)
    much_choice = self.driver.find_element_by_xpath(
        "//android.widget.CheckBox[contains(@resource-id,'checkBox')]")
    # log.recordLog(much_choice.text,much_choice.tag_name)
    much_choice.click()
    comfirm = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'include_title_tv_save')]")
    comfirm.click()
    sleep(3)

    # 获取第33题，多选
    answer_thirty_three = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    # log.recordLog(answer_thirty_three.text,answer_thirty_three.tag_name)
    answer_thirty_three.click()
    send_xz = self.driver.find_element_by_xpath(
        "//android.widget.Button[contains(@resource-id,'btn_send_xz')]")
    send_xz.click()
    sleep(3)

    # 获取第34题，单选
    answer_thirty_four = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    # log.recordLog(answer_thirty_four.text,answer_thirty_four.tag_name)
    answer_thirty_four.click()
    send_xz.click()
    sleep(3)

    # 获取第35题，单选
    answer_thirty_five = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    # log.recordLog(answer_thirty_five.text,answer_thirty_five.tag_name)
    answer_thirty_five.click()
    send_xz.click()
    sleep(3)

    # 获取第36题，单选
    answer_thirty_six = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
    # log.recordLog(answer_thirty_six.text,answer_thirty_six.tag_name)
    answer_thirty_six.click()
    send_xz.click()
    sleep(3)
    print '完成既往史'
