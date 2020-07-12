# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:47:10 2020

@author: PREET MODH
"""

from collections import Counter
t=int(input())
for _ in range(t):
    inpt=list(map(int,input().split()))
    mylist=input()
    c_dict=Counter(mylist)
    for i in range(0,inpt[1]):
        c=int(input())
        sum=0
        for x in c_dict.values():
            temp=x-c
            if temp>=0:
                sum=sum+temp
        print(sum)
        
    
    
    
    
   