#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-7-17

@author: Wangchenyang

@现病史问题
"""

checkbox_context = \
    ['有想死的念头',
     '心情不好，不开心',
     '对任何事情都提不起来兴趣，感觉生活没有意思',
     '有过自杀或者伤害自己的表现',
     '睡眠不好，难以入睡',
     '早醒，凌晨就醒来，难以再次入睡',
     '感觉自己很了不起，很厉害',
     '感觉脑子变聪明了，反应更快了',
     '脾气大，很容易被激怒',
     '有伤害他人的想法或行为'
     ]

checkbox_second_context = \
    ['有想死的念头',
     '心情不好，不开心',
     '对任何事情都提不起来兴趣，感觉生活没有意思',
     '有过自杀或者伤害自己的表现',
     '睡眠不好，难以入睡',
     '早醒，凌晨就醒来，难以再次入睡',
     '感觉自己很了不起，很厉害',
     '感觉脑子变聪明了，反应更快了',
     '脾气大，很容易被激怒',
     '与首次发病症状相同'
     ]

checkbox_third_context = \
    ['家庭原因',
     '工作和学业压力',
     '经济压力',
     '夫妻感情不好',
     '意外事故',
     '外伤导致的',
     '无明显原因'
     ]

question_choice = ['1', '2']

title_one = "针对你的病情，是否是第一次到医院就诊？"
""" 1:是跳转 title_nineteen """
""" 2:否跳转 title_two """

title_two = "最早出现这种不舒服的时候有哪些表现？"   # 多选，选项checkbox_context
""" 跳转 title_three """

title_three = "最早出现这种不舒服的时候是否到医院就诊？"
""" 1:就诊过跳转 title_four """
""" 2:没有跳转 title_two """

title_four = "请输入当时就诊医院的名字"     # 文本输入
""" 跳转 title_five """

title_five = "最早出现这种不舒服的时候进行过哪些治疗？"
""" 1:药物治疗跳转 title_six """
""" 2:未曾治疗，自己就好了跳转 title_two """

title_six = "使用的药物或手术名称是"       # 文本输入
""" 跳转 title_seven """

title_seven = "治疗的效果怎样？"
""" 跳转 title_nine """

title_nine = "从最早出现这种不舒服的表现至今，中间有没有好过？"
""" 1:中间好过，但是反复发作过几次跳转 title_ten """
""" 2:中间好了，这次是第二次发作跳转 title_seventeen """
""" 3:断断续续，中间就没好过跳转 title_twenty """

title_ten = "第二次发病至今多少天（或多少月？或多少年）？（要求准确）"      # 文本输入
""" 跳转 title_eleven """

title_eleven = "与首次发病相比，第二次发病时有哪些不一样的症状"        # 多选，选项checkbox_second_context
""" 跳转 title_twelve """

title_twelve = "第二次发病时是否到医院就诊？"
""" 1:就诊过跳转 title_thirteen """
""" 2:没有跳转 title_fourteen """

title_thirteen = "请输入第二次就诊医院的名字"        # 文本输入
""" 跳转 title_fourteen """

title_fourteen = "第二次发病时进行过哪些治疗？"
""" 1:药物治疗跳转 title_fiveteen """
""" 2:未曾治疗，自己就好了跳转 title_eighteen """

title_fiveteen = "请输入第二次治疗时使用的药物或手术名称"      # 文本输入
""" 跳转 title_sixteen """

title_sixteen = "治疗的效果怎样？"
""" 跳转 title_seventeen """

title_seventeen = "本次发病与第二次发病的症状一样吗？"
""" 1:本次发病与第二次发病症状相同跳转 title_eighteen """
""" 2:比之前加重了跳转 title_eighteen """

title_eighteen = "本次发病至今多少天（或多少月？或多少年）？（要求准确）"      # 文本输入
""" 跳转 title_nineteen """

title_nineteen = "这次发病有哪些主要症状"      # 多选，选项checkbox_context
""" 跳转 title_twenty """

title_twenty = "您是由于什么原因导致了这些情况？"
""" 跳转 title_twenty_one """

title_twenty_one = "现在是否还在工作和学习"
""" 1:还在跳转 title_twenty_two """
""" 2:已暂停跳转 title_twenty_three """

title_twenty_two = "工作和学习能力是否有下降？"
""" 1:是跳转 title_twenty_three """
""" 2:没有跳转 title_twenty_four """

title_twenty_three = "多久了？"
""" 跳转 title_twenty_four """

title_twenty_four = "目前有伤人毁物的想法或行动吗？"
""" 跳转 title_twenty_five """

title_twenty_five = "有轻生的想法或行为吗？"
""" 跳转 title_twenty_six """

title_twenty_six = "近期是否有感冒、发烧？"
""" 1:都没有跳转 title_twenty_nine """
""" 2:有感冒和发烧跳转 title_twenty_seven """

title_twenty_seven = "什么时间开始感冒发烧的？"
title_twenty_eight = "测量最高体温多少度？"
title_twenty_nine = "睡眠情况如何？"
title_thirty = "做梦多吗？"
title_thirty_one = "饮食情况怎样？"
title_thirty_two = "大小便是否正常"