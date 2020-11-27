# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:44:12 2020

@author: PREET MODH
"""



for _ in range(int(input())):
    n,k,x,y=map(int,input().split())
    if x==y:
        print('YES')
        continue
    if k==0:
        print('NO')
        continue
    ans='NO'
    i=x
    j=0
    while(j<5000):
            #print(i,end=' ')
            if i==x and j!=0:
                break
            if i==y:
                ans='YES'
                break
            i=(i+k)%n
            j+=1
    #print()
    print(ans)
     