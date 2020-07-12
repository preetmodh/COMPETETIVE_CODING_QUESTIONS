# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:31:52 2020

@author: PREET MODH
"""



input()
a=list(map(int,input().split()))
a.sort()
count=[]
for i in range(len(a)):
    cnt=1
    for j in range(i+1,len(a)):
        if a[j]-a[i]<=1:
            cnt+=1
        else:
            break
    count.append(cnt)
print(max(count))
        
