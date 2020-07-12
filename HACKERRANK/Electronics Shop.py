# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:14:26 2020

@author: PREET MODH
"""


b,n,m=input().split()
k=list(map(int,input().split()))
d=list(map(int,input().split()))
sum=-1
for i in range(len(k)):
    for j in range(len(d)):
        temp=k[i]+d[j]
        if temp>sum and temp<=int(b):
            sum=temp
print(sum)
