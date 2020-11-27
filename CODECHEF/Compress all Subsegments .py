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
    #print(a,'hi')
    while(len(a)>1):
        n=0
        i1=0
        i2=0
        a.sort()
        for i in range(0,len(a)):
            for j in range(i+1,len(a)) :
                temp= a[i] ^ a[j]
                if temp>n:
                    
                    i1=i
                    i2=j
                    n=temp
        #print(a,n)
        #print(a,n,i1,i2)
        a.pop(i2)
        a.pop(i1)
        a.append(pof2(n,MOD))
        #print(a)
    #print(a[0])
    a[0]=pof2(a[0],MOD)
    return a[0]
        
        

n=int(input())
a=list(map(int,input().split()))
#a.pop(0)
a=subl(a)
st=[]
#for i in a:
 #   print(i)
    #st.append(pof2(max(i),MOD))
s=0
for i in range(len(a)):
            s = (s + findsum(a[i]))%MOD
print(s - 1)