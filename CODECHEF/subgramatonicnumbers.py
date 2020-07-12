# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 16:57:19 2020

@author: PREET MODH
"""


def gen_strobogrammatic(n):

    result = helper(n, n)
    return result


def helper(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8","2","5"]
    middles = helper(n-2, length)
    result = []
    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
        result.append("2" + middle + "2")
        result.append("5" + middle + "5")
    return result
n=int(input())
for j in range(n):
    t=int(input())    
    a=[]
    for i in range(1,8):
        a.extend(gen_strobogrammatic(i))
    for i in range(len(a)):
        a[i]=int(a[i])
    a.sort()
    print(a[t-1])