# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 19:56:20 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    a=list(map(int,input().split()))
    e=0
    o=0
    for i in a:
        if i%2==0 and i!=0:
            e+=1
        else:
            o+=1
    if a.count(0)==1:
        if e==2 or e==3:
            print('Yes')
        else:
            print('No')
            
    elif a.count(0)==2:
        if e==2 or e==1:
            print('Yes')
        else:
            print('No')
    
    elif a.count(0)==3 or a.count(0)==4:
            print('Yes')
            
    else:
        if (e==3 or e==4) or (o==3):
            print('Yes')
        else:
            print('No')
    