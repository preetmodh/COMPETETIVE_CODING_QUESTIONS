# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:12:12 2020

@author: PREET MODH
"""


    
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    temp=0
    sum=0
    i=0
    sum1=0
    while(temp<=sum):
        temp=temp+k
        if i<len(a):
            sum=sum+a[i]
            i+=1
            if i==len(a)-2:
                sum1=sum
        else:
            i=i + (a[i-1] + (sum1 - k*(i-1)))//k
            break
    print(i)