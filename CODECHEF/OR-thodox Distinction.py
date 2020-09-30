# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 21:45:53 2020

@author: PREET MODH
"""


def subarrayBitwiseOR(A): 
  
    res = set() 
    pre = {0} 
  
    for x in A: 
        pre = {x | y for y in pre} | {x} 
        res |= pre 
  
    return len(res)
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans='YES'
    b=subarrayBitwiseOR(a)
    if b==(n*(n+1))/2:
        pass
    else:
        ans='NO'
    print(ans)