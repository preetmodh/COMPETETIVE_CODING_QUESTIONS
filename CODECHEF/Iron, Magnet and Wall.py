# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 10:06:45 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,k=map(int,input().split())
    a=input().split('X')
    ans=0
    for s in a:
        mtem=0
        item=0
        cnt=0
        while(True):
            m=s.find('M',mtem,len(s))
            i=s.find('I',item,len(s))
            if m==-1 or i==-1:
                break
            if m>i:
                p=k+1 - abs(m-i) - s[i:m].count(':')
            else:
                p=k+1 - abs(m-i) - s[m:i].count(':')
            #print(p)
            if p>0:
                ans+=1
                mtem=m+1
                item=i+1
            else:
                if i>m:
                    mtem=m+1
                if m>i:
                    item=i+1
    print(ans)
    