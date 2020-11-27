# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:51:33 2020

@author: PREET MODH
"""
import math

MOD=998244353

def subsetsum(array,num):

    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:],(num - array[0])) 
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)
            


n=int(input())
a=list(map(int,input().split()))
q=int(input())
x=list(map(int,input().split()))
d={}
for i in range(len(a)):
    d[a[i]]=i
for i in x:
    x=x%MOD
    t=subsetsum(a,x)
    il=[]
    for j in t:
        il.append(d[j])
    il.sort()
    y=0
    for i in il:
        y = y + pow(2,i)
    y1 = y % ( pow(2,60) )
    y2 = math.floor( y/( pow(2,60) ) ) % ( pow(2,60) )
    y3 = math.floor( y/( pow(2,120) ) ) % ( pow(2,60) )
    y4 = math.floor( y/( pow(2,180) ) ) % ( pow(2,60) )
    print(y1,y2,y3,y4,end=' ')
    print()
    
    
    
    
    
    
    