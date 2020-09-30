# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:11:38 2020

@author: PREET MODH
"""
for _ in range(int(input())):
    n,c,k=map(int,input().split())
    c=[]
    for i in range(n):
        t=list(map(int,input().split()))
        c.append(t[2])
    cnt=[]
    for i in list(set(c)):
        if c.count(i)>2:
            cnt.append([i,c.count(i)])
    v=list(map(int,input().split()))
    cnt.sort(key = lambda x: x[1],reverse=True)
    ans=0
    i=0
    while(True):
        if v[cnt[0][0]-1]<=k and k!=0:
            cnt[0][1]=cnt[0][1]-1
            k=k-v[cnt[0][0]-1]
            cnt.sort(key = lambda x: x[1],reverse=True)
        else:
            break
        i=+1
    for i in range(len(cnt)):
            ans =ans+int((cnt[i][1]*(cnt[i][1]-1)*(cnt[i][1]-2)))//6
    print(ans)
        
