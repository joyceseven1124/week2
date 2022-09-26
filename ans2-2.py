# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:27:28 2022

@author: 劉佳怡
"""


def avg(data):
# 請用你的程式補完這個函式的區塊
    
#將data回傳Tuple元組
    for i in data.items():
        # x 是將data.items()的元組存入
        x = i
            
    money = 0
    average = 0
    for a in range(0,len(x[1])) :
        if (x[1][a]["manager"] == False):
            money = money + x[1][a]["salary"]
        average = money / (len(x[1])-1)
    print(average)

avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
}) # 呼叫 avg 函式
