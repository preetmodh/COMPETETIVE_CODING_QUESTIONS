# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:58:32 2020

@author: PREET MODH
"""

a = list(map(int,input().split()))
b = 'abcdefghijklmnopqrstuvwxyz'
dict1=dict( zip( list(b),a))
temp=0
ans=0
s=input()
for i,j in dict1.items():
    if i in s:
        temp=j
    if temp>ans:
        ans=temp
print(len(s)*ans)
        
    
