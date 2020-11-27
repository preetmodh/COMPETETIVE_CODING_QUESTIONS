# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:36:48 2020

@author: PREET MODH
"""


def isTwo(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
             
    return True

for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(n)
    elif isTwo(n):
        print(-1)
    else:
        a=[]
        i=n
        while(i>3):
            if isTwo(i-1):
                a.append(i-1)
                a.append(i)
                i=i-2
            else:
                a.append(i)
                i=i-1
        a.append(1)
        a.append(3)
        a.append(2)
        a.reverse()
        print(' '.join(map(str,a)))