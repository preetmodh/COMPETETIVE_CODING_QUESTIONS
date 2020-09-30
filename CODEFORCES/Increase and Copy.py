# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:03:54 2020

@author: PREET MODH
"""

import math
def isPerfectSquare(x): 
   
    sr = math.sqrt(x) 
    
    return ((sr - math.floor(sr)) == 0) 

for _ in range(int(input())):
    n=int(input())
    ans=math.sqrt(n)*2 - 1
    if isPerfectSquare(n):
        ans=ans-1
    print(int(ans))