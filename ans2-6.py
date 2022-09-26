# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 19:57:26 2022

@author: 劉佳怡
"""

def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    count = 0
    maxNum = 0
    for i in nums:
        if(i == 1):
            if(count > maxNum):
                maxNum = count
            count = 0
            continue
        else :
            count += 1
            if(count > maxNum):
                maxNum = count
    print(maxNum)
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3