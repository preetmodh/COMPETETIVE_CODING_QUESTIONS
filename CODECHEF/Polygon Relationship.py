# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:16:08 2020

@author: PREET MODH
"""



for _ in range(int(input())):
    n=int(input())
    for i in range(n):
        x,y=map(int,input().split())
    ans=n
    temp=ans//2
    while(True):
        if temp<3:
            break
        else:
            ans=ans+temp
            temp=temp//2
    print(ans)