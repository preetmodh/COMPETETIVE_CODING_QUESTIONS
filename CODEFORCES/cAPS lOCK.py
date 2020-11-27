# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:10:40 2020

@author: PREET MODH
"""


s=input()
if s[1::].isupper() or len(s)==1:
    print(s.swapcase())
else:
    print(s)