# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:57:04 2020

@author: PREET MODH
"""


t=int(input())
for p in range(0,t):
    input().split()
    a=list(map(int,input().split()))
    l=len(a)
    count=0
    if l%4==2 or l%4==3:
        print('-1')
    else:
        print(int(l/2))
        for i in range(0,l,2):
            j=l-i
            print(i+1,j-1,end=' ')
            print(j)
            print(i+2,j-1,end=' ')
            print(j)
            count=count+2
            if count==int(l/2):
                break
            
    