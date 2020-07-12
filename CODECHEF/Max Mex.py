# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:29:11 2020

@author: PREET MODH
"""

from bisect import bisect_right
for _ in range(int(input())):
    n,m=input().split()
    m=int(m)
    a=list(map(int,input().split()))
    a.sort()
    a.append(0)
    store=[0]
    ans=0
    for i in range(len(a)-1):
        if a[i+1]-a[i]!=1 and a[i+1]!=0:
            store.append(a[i]+1)
    
    if m not in store:
        print('-1')
    else:
        for i in range(len(store)):
            if store[i]==m:
                ind=bisect_right(a,store[i-1]) + 1
        print(len(a)-ind)