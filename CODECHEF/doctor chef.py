# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:26:50 2020

@author: PREET MODH
"""
from bisect import bisect_right

for _ in range(int(input())):
    n,x=input().split()
    x=int(x)
    a=list(map(int,input().split()))
    a.sort()
    days,flag=0,1

    a.insert(0,0)
    maxa=max(a)
    while(True):
        if len(a)==1:
            break
        ind=bisect_right(a,x)
        if ind==1:
            x=x*2
            days+=1
            continue
        else:
            ind=ind-1
            if a[ind]*2>=x:
                x=a.pop(ind)*2
                if x>=maxa:
                    days=days+(len(a))
                    break
                else:
                    days+=1
                    
            else:
                while(True):
                    if x>=maxa:
                        days=days+(len(a)-1)
                        flag=0
                        break
                    if x>=a[ind+1]:
                        x=a.pop(ind+1)*2
                        days=days+1
                        break
                    else:
                        x=x*2
                        days=days+1
                if flag==0:
                    break
                
    print(days)
                    
                    
                
            
            
            