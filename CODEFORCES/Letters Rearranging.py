# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:18:20 2020

@author: PREET MODH
"""


for i in range(int(input())):
     s=input()
     if len(set(s))==1:
         print(-1)
     else:
         print(''.join(sorted(s)))