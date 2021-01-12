# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 22:07:49 2020

@author: PREET MODH
"""

t=int(input())
for T in range(t):
    nu=int(input())
    fuel=list(map(int,input().split()))
    coin=list(map(int,input().split()))
    a=[]
    for i in range(len(coin)):
        a.append((coin[i],fuel[i]))
    sorta=sorted(a)
    cnt=0
    ans=0
    for i in range(len(sorta)):
        if cnt>=nu:
            break
        if sorta[i][1]!=0:
            if cnt+sorta[i][1]>nu:
                b=nu-cnt
                cnt=nu
            else:
                cnt+=sorta[i][1]
                b=sorta[i][1]
            ans+=b*sorta[i][0]
    print(ans)