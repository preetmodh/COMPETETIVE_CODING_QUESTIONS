# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 18:07:30 2020

@author: PREET MODH
"""

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    temp=list(set(a))
    b=[]
    for i in range(len(temp)):
        if a.count(temp[i])==1:
            continue
        else:
            b.append(a.count(temp[i]))
    count=0
    cost=k
    cost1=k
    s=set()
    flag=0
    for i in b:
        cost1=cost1+i
    for i in range(len(a)):
        if a[i] in s:
            count+=k
            s.clear()
            s.add(a[i])
            flag=0
        else:
            cost=cost+count
            count=0
            s.add(a[i])
            flag=1
    if flag==0:
        cost=cost+count
    if cost1==k:
        cost1=10000000000000000000000000000000000001
    print(min(cost,cost1))
            
    
