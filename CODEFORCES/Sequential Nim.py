# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:19:05 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans='First'
    if len(a)==a.count(1):
        if a.count(1)%2==0:
            ans='Second'
    else:
        for i in range(0,len(a)):
            if a[i]==1:
                if ans=='First':
                    ans='Second'
                else:
                    ans='First'
            else:
                break
    print(ans)
            