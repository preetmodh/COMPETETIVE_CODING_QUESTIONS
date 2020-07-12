# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:17:22 2020

@author: PREET MODH
"""


n=int(input())
a=[2]
temp=5
for i in range(1,n):
    temp=(temp//2)*3
    a.append(temp)
ans=2
for i in range(1,len(a)):
    ans=ans+a[i]//2
print(ans)
