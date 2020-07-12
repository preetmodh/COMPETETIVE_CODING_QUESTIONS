# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:17:19 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(len(a)-1):
        ans=ans+abs(a[i]-a[i+1]) - 1
    print(ans)
        