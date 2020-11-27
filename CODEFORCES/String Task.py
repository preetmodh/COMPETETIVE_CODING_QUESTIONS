# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:06:38 2020

@author: PREET MODH
"""


s=input()
d=list('aeiouy')
s=list(s.lower())
i=0
while(i<len(s)):
    if s[i] in d:
        s.pop(i)
        i-=1
    i+=1
s.insert(0,'')
print('.'.join(s))
