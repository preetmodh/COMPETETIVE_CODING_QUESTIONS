# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 13:34:15 2020

@author: PREET MODH
"""


n=int(input())
s=list(input())
ans=''
if len(s)%2!=0:
    i=0
    while(len(s)!=0):
        if i%2==0:
            ans = ans + s[0]
            s.pop(0)
        else:
            ans = s[0] + ans
            s.pop(0)
        i+=1
else:
    i=0
    while(len(s)!=0):
        if i%2==0:
            ans = s[0] + ans
            s.pop(0)
        else:
            ans = ans + s[0]
            s.pop(0)
        i+=1
print(ans)