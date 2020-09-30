# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:06:20 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a=set(a)
    b=set(b)
    c=set()
    if len(a)<len(b):
        c=a.intersection(b)
    else:
        c=b.intersection(a)
    if len(c)==0:
        print('NO')
    else:
        c=list(c)
        print('YES')
        print(1,c[0],end=' ')
        print()