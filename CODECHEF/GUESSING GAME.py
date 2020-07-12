# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:37:18 2020

@author: PREET MODH
"""

n=int(input())
l=1
r=n

m1=(l+r)//2
m2=m1+1
while(True):
    print(m1);
    ans=input()
    if(ans=='E'):
        break
    print(m2);
    ans2=input()
    if(ans2=='E'):
        break
    elif(ans=='L' and ans2=='L'):
        r=m1;
        m1=(l+r)//2;
        m2=m1+1;
    elif(ans=='G' and ans2=='G'):
        l=m2;
        m1=(l+r)//2;
        m2=m1+1;