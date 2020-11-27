# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 17:50:53 2020

@author: PREET MODH
"""
from collections import Counter
a=[]
no=1300000
#sieve of eratosthenes

def primes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    
    for p in range(2, n+1): 
        if prime[p]: 
            a.append(p)
primes(no)

for _ in range(int(input())):
    input()
    b=list(map(int,input().split()))
    
    c=dict(Counter(b))
    i=0
    for j in c:
        c[j]=a[i]
        i+=1
    for x in range(len(b)):
        b[x]=c[b[x]]
    print(' '.join(map(str,b)))
       