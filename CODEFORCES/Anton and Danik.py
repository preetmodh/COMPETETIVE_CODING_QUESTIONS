# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:20:11 2020

@author: PREET MODH
"""


n=int(input())
a=list(input())
if a.count('A')>a.count('D'):
    print('Anton')
elif a.count('D')>a.count('A'):
    print('Danik')
else:
    print('Friendship')