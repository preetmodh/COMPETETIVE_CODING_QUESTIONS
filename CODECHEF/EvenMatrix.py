# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:58:39 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n=int(input())
    odd=list(range(1,n**2 +1,2))
    even=list(range(2,n**2 + 1,2))
    count,i,row=0,0,1
    if n%2==0:
        while(count!=n**2):
            if row%2!=0:
                print(odd[i],even[i],end=' ')
            else:
                print(even[i],odd[i],end=' ')
            count=count+2
            if count%n==0:
                print()
                row=row+1                
            i=i+1
    else:
        for i in range(1,n**2+1):
            print(i,end=' ')
            if i%n==0:
                print()