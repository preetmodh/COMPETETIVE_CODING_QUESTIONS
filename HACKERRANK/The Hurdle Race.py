# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:46:08 2020

@author: PREET MODH
"""


n,k=input().split()
k=int(k)
a=list(map(int,input().split()))
if max(a)-k<1:
    print(0)
else:
    print(max(a)-k)
