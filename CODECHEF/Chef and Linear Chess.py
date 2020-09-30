# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:51:37 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=-1
    cnt=10000000000
    for i in a:
        if k%i==0:
            if (k/i - 1)<cnt:
                cnt=k/i - 1
                ans=i
    print(ans)
        