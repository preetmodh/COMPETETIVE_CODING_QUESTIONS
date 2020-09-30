# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:15:48 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,k=map(int,input().split())
    if k>=n:
        print(k-n)
    else:
        if abs(k-n)%2==0:
            print(0)
        else:
            print(1)