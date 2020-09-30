# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:59:39 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,k=map(int,input().split())
    if n%9==0:
        n=n//9
    else:
        n=n//9 + 1
    if k%9==0:
        k=k//9
    else:
        k=k//9 + 1
    if k<=n:
        print(1,k,end=' ')
        print()
    else:
        print(0,n,end=' ')
        print()
    