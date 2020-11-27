# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:29:16 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n=int(input())
    s=input()
    if s[-1] not in s[:len(s)-1:]:
        print('NO')
    else:
        print('YES')