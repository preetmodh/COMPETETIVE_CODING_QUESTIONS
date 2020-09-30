# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:39:38 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[]
    for i in range(2*n):
        a.append(list(map(int,input().split())))
    if m%2!=0:
        print('NO')
    else:
        flag=0
        for i in range(0,len(a),2):
            if a[i][1]==a[i+1][0]:
                flag=1
                break
        if flag==1:
            print('YES')
        else:
            print('NO')