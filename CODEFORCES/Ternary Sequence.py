# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:24:03 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    c1=list(map(int,input().split()))
    c2=list(map(int,input().split()))
    ans=0
    if c1[2]==0 or c2[1]==0:
        print(0)
    elif c2[1]<=c1[2]:
        print(2*c2[1])
    else:
        ans=2*c1[2]
        c2[1]=c2[1]-c1[2]
        if c1[0]<c2[2]:
            ans=ans - min(c1[1],c2[2])*(2)
        if ans<0:
            ans=0
        print(ans)
        