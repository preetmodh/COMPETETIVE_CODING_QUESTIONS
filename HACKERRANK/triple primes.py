# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:48:09 2020

@author: PREET MODH
"""
def Primes(n): 
    MAX=1000001
    primes = [True]*MAX
    primes[0]=False
    primes[1]=False
    i=2
    while (i*i <= MAX): 
        if (primes[i] == True): 
            for j in range(i**2,MAX,i): 
                primes[j] = False
        i=i+1
    return primes
    
            
            
n=int(input())
a=Primes(n)
primes=[]
for p in range(n + 1): 
        if a[p]:
            primes.append(p)
count=0
for j in range(1,len(primes)-1):
    if primes[j+1]-primes[j]==2:
        XOR=primes[0]^primes[j]
        if (XOR in primes and XOR != primes[0] and XOR != primes[j]):
            count=count+1
print(count)
        
    