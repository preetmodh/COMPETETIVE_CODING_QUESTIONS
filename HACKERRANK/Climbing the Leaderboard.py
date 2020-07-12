# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:54:25 2020

@author: PREET MODH
"""

import bisect

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=list(set(a))
c.sort()
d=[]
for i in range(len(b)):
    print((len(c)+1)-(bisect.bisect_right(c, b[i])))
