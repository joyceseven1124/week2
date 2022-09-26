# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 17:01:58 2022

@author: 劉佳怡
"""

def twoSum(nums, target):
    # your code here
    for i in nums :
        ans = 0
        ans = target - i
        if(ans in nums):
            ansIndex1 = nums.index(ans)
            ansIndex2 = nums.index(i)
            return[ansIndex2,ansIndex1]
        
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
