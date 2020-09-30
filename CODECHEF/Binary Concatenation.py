# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 21:23:41 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        print(a[0])
    else:
        b=[]
        for i in range(len(a)):
            for j in range(len(a)):
                binx=bin(a[i]).replace("0b", "")
                binx=binx.lstrip('0')
                biny=bin(a[j]).replace("0b", "")
                biny=biny.lstrip('0')
                
                binxy=binx+biny
                binyx=biny+binx
                
                b.append(int(binxy,2)-int(binyx,2))
        print(max(b))
    
    
    
    