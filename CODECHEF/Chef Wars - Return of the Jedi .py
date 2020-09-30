# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:28:05 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    h,p=map(int,input().split())
    while(True):
        h=h-p
        if h<=0:
            h=0
            break
        p=p//2
        if p<=0:
            p=0
            break
    if h==0:
        print(1)
    else:
        print(0)
        