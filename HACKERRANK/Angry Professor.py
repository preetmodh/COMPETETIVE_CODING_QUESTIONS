# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:12:27 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,k=input().split()
    k=int(k)
    a=list(map(int,input().split()))
    count=0
    for i in range(len(a)):
        if a[i]<=0:
            count+=1
    if count<k:
        print('YES')
    else:
        print('NO')
