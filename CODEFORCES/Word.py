# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:11:51 2020

@author: PREET MODH
"""


s=input()
countl=0
countu=0
for i in s:
      if(i.islower()):
            countl=countl+1
      elif(i.isupper()):
            countu=countu+1
if countu>countl:
    print(s.upper())
else:
    print(s.lower())