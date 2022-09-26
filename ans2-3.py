# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:17:43 2022

@author: 劉佳怡
"""
def func(a):
# 請用你的程式補完這個函式的區塊
    def func2(b,c):
        result = 0
        result =  a+b*c
        print(result)
    return func2
    
    
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果
