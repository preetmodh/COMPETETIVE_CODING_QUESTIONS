# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 09:59:37 2020

@author: PREET MODH
"""


n,k,q=input().split()
k=int(k)
a=list(map(int,input().split()))
for i in range(k):
    a.insert(0,a[-1])
    a.pop(-1)
for q in range(int(q)):
    m=int(input())
    print(a[m])
    
    
