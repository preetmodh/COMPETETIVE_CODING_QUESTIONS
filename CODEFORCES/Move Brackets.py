# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:30:53 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n=int(input())
    s=input()
    while(s.find('()')!=-1):
        s=s.replace('()','')
    print(len(s)//2)