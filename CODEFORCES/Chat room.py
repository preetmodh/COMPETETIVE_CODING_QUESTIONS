# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:01:23 2020

@author: PREET MODH
"""


s=input()
h='hello'
a=[]
a.append(s.find('h'))
a.append(s.find('e',a[0]+1,len(s)))
a.append(s.find('l',a[1]+1,len(s)))
a.append(s.find('l',a[2]+1,len(s)))
a.append(s.find('o',a[3]+1,len(s)))
temp=sorted(a)
if -1 in a:
    print('NO')
elif temp==a:
    print('YES')
else:
    print('NO')