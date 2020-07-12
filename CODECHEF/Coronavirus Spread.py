# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:47:10 2020

@author: PREET MODH
"""


t=int(input())
for _ in range(t):
    int(input())
    count=1
    b=[]
    a=list(map(int,input().split()))
    a.append(50)
    for i in range(0,len(a)-1):
        if (a[i+1]-a[i])<=2:
            count=count+1
        else:
            b.append(count)
            count=1
    print(min(b),end=' ')
    print(max(b))