# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:48:48 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        b=list(map(int,input().split()))
        a.append(b)
    cnt=0
    for i in range(n-1,0,-1):
        lasts=a[i][i-1] + 1
        if lasts!=a[i][i]:
            cnt+=1
            for x in range(i+1):
                for y in range(x,i+1):
                    a[y][x],a[x][y]=a[x][y],a[y][x]
    print(cnt+1)