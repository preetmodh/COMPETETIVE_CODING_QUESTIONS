# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:25:40 2020

@author: PREET MODH
"""


a=list(input())
s=['a','e','i','o','u']
ans='YES'
if (a[-1] not in s) and a[-1]!='n':
    ans='NO'
else:
    for i in range(len(a)-1):
        if a[i]=='n':
            continue
        if (a[i] not in s):
            if a[i+1] in s:
                continue
            else:
                ans='NO'
print(ans)
            