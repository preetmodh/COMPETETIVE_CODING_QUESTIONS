# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:17:36 2020

@author: PREET MODH
"""


s=list(input())
t=list(input())
s.reverse()
t.reverse()
ans=0
if s[0]!=t[0]:
    ans=len(s) + len(t)
else:
    cnt=0
    for i in range(min(len(s),len(t))):
        if s[i]==t[i]:
            cnt+=1
        else:
            break
    ans=(len(s) - cnt) + (len(t) - cnt)
print(ans)
