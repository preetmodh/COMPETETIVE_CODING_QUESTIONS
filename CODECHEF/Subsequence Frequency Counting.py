# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 20:06:53 2020

@author: PREET MODH
"""
from itertools import combinations
from collections import Counter 
  
def most_frequent(List): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0][0]
def give(a):
    return pow(2,a,1000000007)

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if len(a)==len(set(a)):
        b=list(map(give,range(n-1,-1,-1)))
        for i in b:
            print(i,end=' ')
        print()
    else:
        comb=[]
        cnt=[0]*(n+1)
        b=[]
        for i in range(1,n+1):
            comb.extend(combinations(a,i))
        for i in range(len(comb)):
            comb[i]=list(comb[i])
        for i in range(len(comb)):
            if len(comb[i])==len(set(comb[i])):
                b.append(min(comb[i]))
            else:
                b.append(most_frequent(comb[i]))
        for i in range(1,len(cnt)):
            cnt[i]=b.count(i)
        cnt.pop(0)
        for i in cnt:
            print(i,end=' ')
        print()
        