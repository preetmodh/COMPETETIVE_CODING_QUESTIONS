# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 21:53:01 2020

@author: PREET MODH
"""

from collections import Counter

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cost=0
    flag=1
    
    
    a.sort()   
    b.sort()
    if a==b:
        cost=0
        flag=0
    if flag==1:
        temp=a+b
        temp.sort()
        dtemp=dict(Counter(temp))
        for i in dtemp.values():
            if i%2!=0:
                flag=0
                cost=-1
                break
        if flag==1:
            a1=[]
            b1=[]
            da=dict(Counter(a))
            db=dict(Counter(b))
            a=list(set(a))
            b=list(set(b))
            for i in range(len(a)):
                if (da[a[i]]-(dtemp[a[i]])//2)>=0:
                    for j in range((da[a[i]]-(dtemp[a[i]])//2)):
                        a1.append(a[i])
            for i in range(len(b)):
                if (db[b[i]]-(dtemp[b[i]])//2)>=0:
                    for j in range((db[b[i]]-(dtemp[b[i]])//2)):
                        b1.append(b[i])
                
                    
            if len(b1)!=len(a1):
                cost=-1
                flag=0
            if len(a1)==0:
                cost=0
                flag=0
            if flag==1:
                a1.sort()
                b1.sort(reverse=True)
                small=min(temp)
                for i in range(len(a1)):
                    cost=cost+min(2*small,min(a1[i],b1[i]))
    print(cost)
        
            