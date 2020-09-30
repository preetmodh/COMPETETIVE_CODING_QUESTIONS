# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:30:35 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,x=map(int,input().split())
    cnt=1
    i=0
    f=2
    while(True):
        if f>=n:
            break
        f=f+x
        cnt+=1
    print(cnt)
        