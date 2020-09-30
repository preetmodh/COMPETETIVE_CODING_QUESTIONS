# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:34:56 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    i=0
    if max(a)>k:
        print(-1)
    else:
        i=0
        sum=0
        cnt=1
        while(True):
            sum=sum+a[i]
            if sum<=k :
                i+=1
            else:
                cnt+=1
                sum=0
            if i>len(a)-1:
                break
        print(cnt)
            
    
    
    
    
    
    