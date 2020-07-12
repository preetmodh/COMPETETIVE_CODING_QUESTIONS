# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 21:53:01 2020

@author: PREET MODH
"""
def recursiveBinarySearch(aList, target, start, end):
    if end-start+1 <= 0:
        return -1
    else:
        midpoint = start + (end - start) // 2
        try:
            if aList[midpoint] == target:
                return midpoint
        except IndexError:
            pass
        else:
            if target < aList[midpoint]:
                return recursiveBinarySearch(aList, target, start, midpoint-1)
            else:
                return recursiveBinarySearch(aList ,target, midpoint+1, end)


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cost=0
    count=1
    i=0
    flag=1
    flag2=0
    
    
    a.sort()   
    b.sort()
    if a==b:
        cost=0
        flag=0
            
    if flag==1: 
        temp=a+b
        temp.sort()
        temp.append(temp[-1]+1)
        while(i<len(temp)-1):
            if temp[i]==temp[i+1]:
                count+=1
            else:
                if count%2!=0:
                    cost=-1
                    flag=0
                    break
                count=1
            i=i+1
            
    if flag==1:
        temp=a+b
        temp.sort()
        temp2=[]
        for i in range(0,len(temp),2):
            temp2.append(temp[i])

        for i in range(len(temp2)):
            ind=recursiveBinarySearch(a,temp2[i],0,len(a))
            if ind==-1:
                continue
            else:
                if ind!=None:
                    a.pop(ind)

        for i in range(len(temp2)):
            ind=recursiveBinarySearch(b,temp2[i],0,len(b))
            if ind==-1:
                continue
            else:
                if ind!=None:
                    b.pop(ind)
                
        if len(b)!=len(a):
            cost=-1
            flag=0
        if len(a)==0:
            cost=0
            flag=0
        if flag==1:
            a.sort()
            b.sort(reverse=True)
            small=min(temp)
            for i in range(len(a)):
                cost=cost+min(2*small,min(a[i],b[i]))
    print(cost)