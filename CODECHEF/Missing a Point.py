# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:27:30 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n=int(input())
    xco,yco=[],[]
    flagx,flagy,xans,yans=1,1,0,0
    for x in range(4*n-1):
        x,y=input().split()
        xco.append(int(x))
        yco.append(int(y))
        
    xco.sort(),yco.sort()
    xco.append(xco[-1]+1),yco.append(yco[-1]+1)
    
    countx,county,i=1,1,0
    while(i<len(xco)-1):
        if flagx==1:
            if xco[i]==xco[i+1]:
                countx+=1
            else:
                if countx%2!=0:
                    xans=xco[i]
                    flagx=0
                countx=1
        if flagy==1:
            if yco[i]==yco[i+1]:
                county+=1
            else:
                if county%2!=0:
                    yans=yco[i]
                    flagy=0
                county=1
        if flagx==0 and flagy==0:
            break
        i=i+1
    print(xans,yans,end=' ')
        