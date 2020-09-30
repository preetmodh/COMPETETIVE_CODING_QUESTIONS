# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:31:36 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    input()
    a=list(map(int,input().split()))
    i=0 
    l=len(a)
    while(i<l):
    	if(a[i]==0):
    		a.remove(a[i])	
    		l=l-1   
    		continue
    	i = i+1
    print(len(set(a)))