# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:36:55 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    input()
    a=list(map(int,input().split()))
    tmoney=0
    count=0
    if a[0]>5:
        print('NO')
    else:
        for i in range(len(a)):
            if a[i]==5:
                tmoney=tmoney+a[i]
            else:
                if (a[i]-5)>tmoney:
                    print('NO')
                    break
                if 15 in a:
                        tmoney=tmoney - (a[i]-5) + 5
                else:
                    tmoney=tmoney - (a[i]-5)
            count+=1
    if count==len(a):
        print('YES')