# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:52:16 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,t=map(int,input().split())
    a=list(map(int,input().split()))
    s=set()
    for j in range(len(a)):
        if (t - a[j]) not in s:
            s.add(a[j])
            a[j]=1
        else:
            if a[j] in s:
                s.remove(a[j])
            a[j]=0
    print(' '.join(map(str,a)))
    