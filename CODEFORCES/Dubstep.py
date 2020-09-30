# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:33:06 2020

@author: PREET MODH
"""


#print(' '.join(input().split('WUB')))
s=list(input())
for i in range(len(s)-2):
     if s[i]=='W' and s[i+1]=='U' and s[i+2]=='B':
         s[i],s[i+1],s[i+2]='0','0','0'
for i in range(len(s)):
    if s[i]=='0':
        continue
    if s[i-1]=='0' and s[i]!='0':
        print(' ',end='')
    print(s[i],end='')
print()
               