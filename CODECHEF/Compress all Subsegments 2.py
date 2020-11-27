# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:01:45 2020

@author: PREET MODH
"""

import math 

MOD=998244353

def pof2(n,m): 
    if n==0:
        return 0
    else:
        p = int(math.log(n, 2)) 
        return pow(2,p,m)  

def subl(A):  
   B = [] 
   for i in range(len(A) + 1):    
      for j in range(i + 1, len(A) + 1):          
         sub = A[i:j] 
         if len(sub)>0:
             B.append(sub) 
   return B 

def findsum(a):
    print(a,'hi')
    while(len(a)>1):
        a.sort()
        n=a[0] ^ a[-1]
        a.pop(0)
        a.pop(-1)
        a.append(pof2(n,MOD))
        #print(a)
    print(a[0])
    a[0]=pof2(a[0],MOD)
    return a[0]
        
        

n=int(input())
a=list(map(int,input().split()))
a=[0,1,2,2,4,4,4,4,8,8]
a=subl(a)
st=0
for i in a:
    st=st+sum(i)
s=0
for i in range(len(a)):
    if len(a[i])!=1:
        s = (s + findsum(a[i]))%MOD
    else:
        s = (s + (a[i][0]))%MOD
print(s)