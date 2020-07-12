# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:52:10 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    n=int(input())
    board=[]
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append('X')
    count,i,flag=0,0,0
    while(True):
        if i%2==0:
            for j in range(0,8,1):
                board[j][i]='.'
                count+=1
                if count==n:
                    flag=1
                    break
            if flag==1:
                break
        else:
            for j in range(7,-1,-1):
                board[j][i]='.'
                count+=1
                if count==n:
                    flag=1
                    break
            if flag==1:
                break
            
        i+=1
    board[0][0]='O'
    for i in range(8):
        for j in range(8):
            print(board[i][j],end='')
        print()
    
            
        
            