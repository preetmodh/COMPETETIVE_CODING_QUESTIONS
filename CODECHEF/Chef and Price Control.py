# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:01:11 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,m=input().split()
    m=int(m)
    a=list(map(int,input().split()))
    sum1=0
    sum2=0
    for i in range(len(a)):
        sum1=sum1+a[i]
        if a[i]>m:
            a[i]=m
        sum2=sum2+a[i]
    print(sum1-sum2)