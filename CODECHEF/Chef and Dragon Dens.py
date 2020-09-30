# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 10:09:27 2020

@author: PREET MODH
"""


n,q=input().split()
h=list(map(int,input().split()))
a=list(map(int,input().split()))
for _ in range(int(q)):
    x,b,c=input().split()
    step,ans,x,b,c=0,0,int(x),int(b),int(c)
    if x==1:
        a[b-1]=c
    else:
        if b>c:
            step=1
            cc=c+1
        else:
            step=-1
            cc=c-1
        b,c=c-1,b-1
        maxv=h[b]
        ans=a[b]
        for i in range(b,cc,step):
            if h[i]>=h[c] and i!=c:
                ans=-1
                break
            if h[i]>maxv:
                ans=ans+a[i]
            maxv=max(maxv,h[i])
        print(ans)