# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 16:15:53 2022

@author: 劉佳怡
"""

def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
    outterbigNum = 0
    for i in range (0, len(nums)):
        if (len(nums) == 2) :
            outterbigNum=nums[0] * nums[1]
            break
        else:
            x = nums[i]
            innerbigNum = 0
            for a in range(0, len(nums)):
                if(a != i) :
                    result = x * nums[a]          
                    if(result > innerbigNum):
                        innerbigNum = result
            if (innerbigNum > outterbigNum):
                outterbigNum = innerbigNum    
    print(outterbigNum)
    
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

