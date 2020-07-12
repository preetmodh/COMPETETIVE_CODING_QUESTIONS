# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:40:18 2020

@author: PREET MODH
"""
from itertools import combinations
try:
    for t in range(int(input())):
        a=input()
        b=input()
        sbi=set()
        for i in range(int(input())):
            s,bi=input().split()
            sbi.add((s,int(bi)))
        MIN=100
        for i,j in sbi:
            if(len(i)<MIN):
                MIN=len(i)
            
            
    
        SUMall=[0]
        C=[]
        a=[a[x:y] for x, y in combinations(range(len(a) + 1), r = 2)]
        b=[b[x:y] for x, y in combinations(range(len(b) + 1), r = 2)]
        for i in a+b:
            if len(i)>=MIN:
                C.append(i)
        
        for i in a:
            if len(i)>=MIN:
                for j in b:
                    C.append(i+j)
        a.clear()   
        b.clear()
        index=0
        Count=0
        for z in range(0,len(C)):
            s=C[z]
            Count=0
            for y,u in sbi:
                if y not in s:
                    Count=Count+1
            if Count==len(sbi):
                C.pop(z)
            
        Count=0
        for p in range(0,len(C)):
            st_rsub = C[p]
            SUM=0
            for y,u in sbi:
                while(True):
                    index=st_rsub.find(y,index,len(st_rsub))
                    if index<0:
                        index=0
                        break
                    Count=Count+st_rsub.count(y,index,index+len(y))
                    index=index+(len(y)-1)
                SUM=SUM +Count*u
                Count=0
            if SUM!=0:
                SUMall.append(SUM)
        print(max(SUMall))
except:
    pass