# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:40:01 2020

@author: PREET MODH
"""


n,m=map(int,input().split())
b=[]
for i in range(m):
    b.append(input().split())
a=input()
for i in range(len(b)):
    m=min(len(b[i][0]),len(b[i][1]))
    if m==len(b[i][0]):
        a=a.replace(b[i][1],b[i][0],-1)
    else:
        a=a.replace(b[i][0],b[i][1],-1)
print(a)
