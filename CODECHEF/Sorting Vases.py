# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:24:39 2020

@author: PREET MODH
"""


t=int(input())
for _ in range(t):
    n,m=input().split()
    a=list(map(int,input().split()))
    a.insert(0,'0')
    ac=a.copy()
    for i in range(int(m)):
        x,y=input().split()
        if int(x)>int(y):
            x,y=y,x
        
        if a[int(x)]>a[int(y)]:
            a[int(x)],a[int(y)]=a[int(y)],a[int(x)]
    count=0
    for i in range(0,int(n)):
        for j in range(1,int(n)+1):
            if a[j]!=j:
                a[a[j]], a[j]= a[j],a[a[j]]
                count=count+1
                break
    count1=0
    for i in range(0,int(n)):
        for j in range(1,int(n)+1):
            if ac[j]!=j:
                ac[ac[j]], ac[j]= ac[j],ac[ac[j]]
                count1=count1+1
                break
    print(min(count,count1))
        