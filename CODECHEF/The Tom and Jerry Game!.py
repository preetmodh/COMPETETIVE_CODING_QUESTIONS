# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 17:43:00 2020

@author: PREET MODH
"""
def odd(n):
    if n==0 or n%2!=0:
        return n
    else:
        return odd(n//2)

for _ in range(int(input())):
    TS=int(input())
    if TS%2==0:
        TS=odd(TS)
    print(TS//2)    