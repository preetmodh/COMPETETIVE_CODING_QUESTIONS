# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 09:35:22 2020

@author: PREET MODH
"""

import math

def east(x):
    if (math.gcd(x[0]+2*x[1],x[1])==1) and ((x[0]+2*x[1])%2!=0 and x[1]%2!=0):
        return (x[0]+2*x[1],x[1])
    else:
        return None
def west(x):
    if (math.gcd(x[0]-2*x[1],x[1])==1) and ((x[0]-2*x[1])%2!=0 and x[1]%2!=0):
        return (x[0]-2*x[1],x[1])
    else:
        return None
def north(x):
    if (math.gcd(x[0],x[1]+2*x[0])==1) and (x[0]%2!=0 and (x[1]+2*x[0])%2!=0) and (x[1]+2*x[0])>0:
        return (x[0],x[1]+2*x[0])
    elif (math.gcd(-x[0],-x[1]-2*x[0])==1) and (-x[0]%2!=0 and (-x[1]-2*x[0])%2!=0) and (-x[1]-2*x[0])>0:
        return (-x[0],-x[1]-2*x[0])
    else:
        return None

def south(x):
    if (math.gcd(x[0],x[1]-2*x[0])==1) and (x[0]%2!=0 and (x[1]-2*x[0])%2!=0) and (x[1]-2*x[0])>0:
        return (x[0],x[1]-2*x[0])
    elif (math.gcd(-x[0],-x[1]+2*x[0])==1) and (-x[0]%2!=0 and (-x[1]+2*x[0])%2!=0) and (-x[1]+2*x[0])>0:
        return (-x[0],-x[1]+2*x[0])
    return None

def cal(x):
    a=set()
    a.add(east(x))
    a.add(west(x))
    a.add(north(x))
    a.add(south(x))
    return a

for _ in range(int(input())):
    temp=list(map(int,input().split()))
    start=(temp[0],temp[1])
    end=(temp[2],temp[3])
    if start==end:
        print(0)
        continue
    a=[start]
    ans=set([100000000000000000])

    for i in a:
        temp=(cal(i))
        if end in temp:
            ans.add(1)
        for j in temp:
            temp1=(cal(j))
            if end in temp1:
                ans.add(2)
            for k in temp1:
                temp2=(cal(k))
                if end in temp2:
                    ans.add(3)
                for l in temp2:
                    temp3=(cal(l))
                    if end in temp3:
                        ans.add(4)
                    for m in temp3:
                        temp4=(cal(m))
                        if end in temp4:
                            ans.add(5)
                        for n in temp4:
                            temp5=(cal(n))
                            if end in temp5:
                                ans.add(6)
                            for o in temp5:
                                temp6=(cal(o))
                                if end in temp6:
                                    ans.add(7)
                                for p in temp6:
                                    temp7=(cal(p))
                                    if end in temp7:
                                        ans.add(8)
                                    for q in temp7:
                                        temp8=(cal(q))
                                        if end in temp7:
                                            ans.add(9)
    print(min(ans))
        