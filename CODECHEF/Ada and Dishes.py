# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:14:08 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    if n==1:
        print(a[0])
    else:
        total=0
        b1,b2=a[0],a[1]
        for i in range(2,len(a)):
            diff=abs(b1-b2)
            total+=min(b1,b2)
            b1=diff
            b2=a[i]
        total+=max(b1,b2)
        print(total)
            