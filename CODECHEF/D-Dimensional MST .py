#!/usr/bin/env python
from __future__ import division, print_function
from operator import itemgetter
import os
import sys
from io import BytesIO, IOBase


def main():
    pass


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")



#Class to represent a graph 
class Graph: 

    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = [] 
        

    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 

        
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 


        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

    
    def KruskalMST(self): 

        result =[] 

        i = 0
        e = 0


        self.graph.sort(key=itemgetter(2))

        parent = []
        rank = [] 


        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
    

        while e < self.V -1 : 

            u,v,w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
            cnt=0   
            if x != y: 
                e = e + 1    
                result.append([u,v,w])
                cnt+=1
                self.union(parent, rank, x, y)
            if cnt==(n-1):
                break
        sm=0
        for u,v,weight in result: 
            sm = sm + weight  
        return abs(sm)

    
n,d=sys.stdin.readline().split()
n=int(n)
d=int(d)
s=[]
for i in range(n):
    s.append(input().split())
g = Graph(n)
i=0
while(i<len(s)):
    j=i+1
    while(j<len(s)):
        sm=0
        x=0
        while(x<d):
            sm = sm + abs( int(s[i][x]) - int(s[j][x]) )
            x+=1
        g.addEdge(i,j,-sm)
        j+=1
    i+=1
        
sys.stdout.write(str(g.KruskalMST())) 

