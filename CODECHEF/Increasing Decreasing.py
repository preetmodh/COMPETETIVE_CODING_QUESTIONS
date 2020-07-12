# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 22:16:37 2020

@author: PREET MODH
"""


from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    list1=list(set(a))
    list2=[]
    c=Counter(a)
    temp=c.most_common(1)
    temp[0]=list(temp[0])
    if temp[0][1]>2:
        print('NO')
    else:
        list3=list(c.most_common())
        for x in range(len(list3)):
            list3[x]=list(list3[x])
            for i in range(len(list3[x])-1):
                if (list3[x][i+1]== 2) :  
                    list2.append(list3[x][i])
        list1.sort()
        list2.sort(reverse=True)
        list3.clear()
        for i in list1: 
            list3.append(i)  
        for i in list2 :  
            list3.append(i)

        list3.insert(0,0)
        if list3[-1]==list3[-2]:
            print('NO')
        else:
            print('YES')
            for i in range(1,len(list3)):
                print(list3[i],end=' ')
            print()
