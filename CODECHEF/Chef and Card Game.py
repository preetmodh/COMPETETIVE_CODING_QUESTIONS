# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:28:09 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n=int(input())
    csum,msum,ccnt,mcnt=0,0,0,0
    for x in range(n):
        c,m=input().split()
        csum,msum=0,0
        for i in range(len(c)):
            csum=csum+int(c[i])
        for i in range(len(m)):
            msum=msum+int(m[i])
        if csum>msum:
            ccnt+=1
        elif msum>csum:
            mcnt+=1
        else:
            ccnt+=1
            mcnt+=1
    if ccnt>mcnt:
        print(0,ccnt,end=' ')
        
    elif mcnt>ccnt:
        print(1,mcnt,end=' ')
    
    else:
        print(2,ccnt,end=' ')
    print()
    
    
            