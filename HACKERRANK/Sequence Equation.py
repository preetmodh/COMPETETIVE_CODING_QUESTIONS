# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 09:50:36 2020

@author: PREET MODH
"""


n=int(input())
a=list(map(int,input().split()))
b=[]
for x in range(1,n+1):
    temp=a.index(x)
    b.append(a.index(temp + 1) + 1)
for i in range(len(b)):
    print(b[i])
