# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:19:06 2020

@author: PREET MODH
"""


n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
mx=min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0])
vr=max(b[0],b[2])
if vr>=a[0]:
    i=b.index(vr)
    b[i]=b[i]-a[0]
    if b[i]<=0:
        b[i]=0
    else:
     a[0]=0
else:
    i=b.index(vr)
    a[0]=a[0]-b[i]
    b[i]=0
vs=max(b[0],b[1])
if vs>=a[1]:
    i=b.index(vs)
    b[i]=b[i]-a[1]
    if b[i]<=0:
        b[i]=0
    else:
        a[1]=0
else:
    i=b.index(vs)
    a[1]=a[1]-b[i]
    b[i]=0
vp=max(b[2],b[1])
if vp>=a[2]:
    i=b.index(vp)
    b[i]=b[i]-a[2]
    if b[i]<=0:
        b[i]=0
    else:        
        a[2]=0
else:
    i=b.index(vp)
    a[2]=a[2]-b[i]
    b[i]=0
mn=min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0])
print(mn,mx,end=' ')
print()