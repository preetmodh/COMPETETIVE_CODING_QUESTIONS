# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:54:28 2020

@author: PREET MODH
"""

import bisect

for _ in range(int(input())):
    n,x,p,k=map(int,input().split())
    k,p=k-1,p-1
    cnt=0
    a=list(map(int,input().split()))
    a.sort()
    if x not in a:
        a[k]=x
        cnt=1
    a.sort()
    
    if a[p]==x:
        print(cnt)
        continue
    
    ind=bisect.bisect_left(a,x)
    if p>ind:
        ind=bisect.bisect_right(a,x) - 1

    if ind==k:
        print(-1)
    elif (ind<p and ind>k) or (ind>p  and ind<k):
        print(-1)
    elif (k<p and k>ind) or (k>p  and k<ind):
        print(-1)
    else:
        print(cnt + abs(ind - p))
            
    
    