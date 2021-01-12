# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:25:16 2020

@author: PREET MODH
"""
from fractions import Fraction
n = int(input())
c=0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        top=i*(j+1)
        bottom=j*(i+1)
        s=Fraction(top,bottom)
        
        if s.denominator==s.numerator+1:
            print(i,j,s)
            c+=1
print(c)


        