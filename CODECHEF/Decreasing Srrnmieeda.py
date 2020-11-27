# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:34:38 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    l,r=map(int,input().split())
    if r/l>=2:
        print(-1)
    else:
        print(r)