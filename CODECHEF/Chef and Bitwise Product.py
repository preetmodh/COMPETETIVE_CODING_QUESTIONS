# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:48:56 2020

@author: PREET MODH
"""


t=int(input())
for _ in range(t):
    x,y,l,r=input().split()
    a=[]
    ans=0
    z=0
    for i in range(int(l),int(r)+1):
        temp=(int(x) & i)*(int(y) & i)
        print(i,end=' ')
        print(temp)
        if ans<temp:
            ans=temp
            z=i
            
    print(z)
        