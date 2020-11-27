# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:10:36 2020

@author: PREET MODH
"""


import heapq
class Solution:
    def minCostConnectPoints(self, points):
        heap, c, ans = list(), 0, 0
        parent = [-1]*len(points)
        if len(points) == 1 or not points:
            return 0
        
        i=0
        while(i<len(points)):
            j=i+1
            while(j<len(points)):
                sm=0
                x=0
                while(x<len(points[i])):
                    sm = sm + abs( points[i][x] - points[j][x] )
                    x+=1
                heap.append((-sm, i, j))
                j+=1
            i+=1
        heapq.heapify(heap)
        
        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            parent[px] = py
        
        while c < len(points) - 1:
            d, x, y = heapq.heappop(heap)
            if find(x) != find(y):
                ans += d
                union(x, y)
                c += 1
        return abs(ans)
    
    
n,d=map(int,input().split())
s=[]
for i in range(n):
    s.append(list(map(int,input().split())))
g = Solution()
print(g.minCostConnectPoints(s))
    
    
    