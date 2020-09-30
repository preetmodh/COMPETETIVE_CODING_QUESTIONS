# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:58:55 2020

@author: PREET MODH
"""

import math
for _ in range(int(input())):
    n=int(input())
    c=-(n*(n+1)//2)
    aa=round((-1 + ((math.sqrt(1 - 4*c))/2)))
    bb=math.sqrt(1-4*c)
    if n==3:
        print(2)
    elif ((n*(n+1))//2)%2==0:
        ans=n-aa
        if ((bb)-(int(bb)))==0:
            ans = ans + (aa*(aa-1)//2) + ((n-aa)*(n-aa-1)//2)
        print(round(ans))
    else: 
        print(0)
    