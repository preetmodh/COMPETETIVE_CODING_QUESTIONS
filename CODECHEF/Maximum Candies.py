# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:31:13 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    r,c,x,y=map(int,input().split())
    ans=0
    temp=0
    if r==1 and c==1:
        ans=x
    else:
        if x<=y:
            temp=y-x
            if temp>x:
                temp=x
        else:
            temp=0
            x=y
        if c%2==0:
            ans=ans+x*(r)*(c//2)
            ans=ans+temp*(r)*(c//2)
        else:
            if r%2==0:
                ans=ans+(r//2)*(c//2 +1)*(x)
                ans=ans+(r//2)*(c//2)*(x)
                ans=ans+(r//2)*(c//2 +1)*(temp)
                ans=ans+(r//2)*(c//2)*(temp)
            else:
                ans=ans+(r//2+1)*(c//2 +1)*(x)
                ans=ans+(r//2)*(c//2)*(x)
                ans=ans+(r//2)*(c//2 +1)*(temp)
                ans=ans+(r//2+1)*(c//2)*(temp)
    print(ans)