# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 17:37:06 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    s=input()
    p=input()
    for i in range(len(p)):
        s=s.replace(p[i],'',1)
    a=[]
    for i in s:
        a.append(i)
    a.sort()
    ans=''
    ans1=''
    flag2=1
    for i in range(len(a)):
        if flag2==1:
            if a[i]>p[0]:
                ans=ans+p+a[i]
                flag2=0
            else:
                ans=ans+a[i]
        else:
            ans=ans+a[i]
    if flag2==1:
        ans=ans+p
    
    flag2=1
    for i in range(len(a)):
        if flag2==1:
            if a[i]==p[0]:
                ans1=ans1+p+a[i]
                flag2=0
            else:
                ans1=ans1+a[i]
        else:
            ans1=ans1+a[i]
    if flag2==1:
        ans1=ans1+p
        
    if len(ans)==0:
        ans=p
    print(min(ans,ans1))
    