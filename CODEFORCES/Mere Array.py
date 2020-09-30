
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:35:53 2020
 
@author: PREET MODH
"""
 
import math 
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    temp=a.copy()
    temp.sort()
    m=min(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if a[j]>a[i] and math.gcd(a[j],a[i])==m:
                a[j],a[i]=a[i],a[j]
    if temp==a:
        print('YES')
    else:
        print('NO')
            