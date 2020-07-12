# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:28:39 2020

@author: PREET MODH
"""


n=int(input())
l=1
r=n
flag=0
m=(l+r)//2
while(True):
    while(True):
        print(1);
        ans=input()
        if(ans=='L'):
            break
        if(ans=='E'):
            falg=1
            break
    if flag==1:
        break
    print(m)
    ans=input()
    temp=ans
    ans2=ans
    if(ans2=='E'):
        break
    while(True):
        print(m)
        ans=input()
        if(ans!=temp):
            break
        temp=ans
    if(ans2=='E'):
        falg=1
        break
    elif(ans2=='L'):
        r=m
        m=(l+r)//2;
    elif(ans2=='G' ):
        l=m
        m=(l+r)//2;