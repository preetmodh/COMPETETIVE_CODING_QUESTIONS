# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:23:59 2020

@author: PREET MODH
"""


n=int(input())
a=list(map(int,input().split()))
while(True):
    if len(a)==0:
        break
    else:
        print(len(a))
        sm=(min(a))
        for i in range(len(a)):
            a[i]=a[i]-sm
        while(True):
            if 0 in a:
                ind=a.index(0)
                a.pop(ind)
            else:
                break
