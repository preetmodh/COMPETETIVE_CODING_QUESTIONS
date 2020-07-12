# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:48:50 2020

@author: PREET MODH
"""

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
i,j,k=input().split()
k=int(k)
count=0
for x in range(int(i),int(j)+1):
    x2=x
    x=str(x)
    x=x[::-1]
    dif=abs(x2-int(x))/k
    if is_integer_num(dif):
        count+=1
print(count)
    
