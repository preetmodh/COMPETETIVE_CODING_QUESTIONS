# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 09:59:02 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n,p=input().split()
    n=int(n)
    p=int(p)
    a=[]
    stop=int(((p)*(n*n))/100)

    for i in range(1,n+1):
         print(1,i,1,i,n,end=' ')
         x=int(input())
         if x!=0 :
             for j in range(1,n+1):
                print(1,i,j,i,j,end=' ')
                x=int(input())
                a.append(x)
                
         else:
             if x==0:
                 for i in range(n):
                     a.append(0)

    print(2)
    for i in range(0,len(a)):
        print(a[i],end=' ')
        if(i+1)==len(a):
             y=int(input())
        elif (i+1)%n==0:
            print()
   