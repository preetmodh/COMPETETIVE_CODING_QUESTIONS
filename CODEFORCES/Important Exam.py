# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:43:46 2020

@author: PREET MODH
"""

from collections import Counter

n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(input()))
b=list(map(int,input().split()))
cnt=[]
ans=[]
result=0
for i in range(m):
    temp=[]
    for j in range(n):
        temp.append(a[j][i])
    cnt.append(temp)
for i in range(len(cnt)):
    temp=Counter(cnt[i])
    temp1=temp.most_common(1)[0][0]
    ans.append(temp1)
for i in range(len(ans)):
    result=result + cnt[i].count(ans[i]) * b[i]
print(result)
    
        