# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:57:32 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    ans=0
    for i in range(1,len(a)):
        a[i]=k - a[i]
        a[i]=a[i]//a[0]
        if a[i]>0:
            ans=ans+a[i]
    print(ans)
        