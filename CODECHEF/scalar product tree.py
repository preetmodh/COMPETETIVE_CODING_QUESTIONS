# Python3 implementation of the approach
from collections import deque as queue
import numpy as np

sz = (3*(10**5) + 1)

tree = [[] for i in range(sz)]

vis = [False] * sz

path = [[] for i in range(sz)]

def addEdge(a, b):

    tree[a].append(b)
    tree[b].append(a)

def bfs(node):

    qu = queue()

    qu.append([node, -1])
    vis[node] = True

    while (len(qu) > 0):
        p = qu.popleft()
        
        vis[p[0]] = True

        for child in tree[p[0]]:
            if (vis[child] == False):
                qu.append([child, p[0]])

                for u in path[p[0]]:
                    path[child].append(u)

                path[child].append(p[0])
                


if __name__ == '__main__':

    # Number of vertices
    n,q=map(int,input().split())
    a=tuple(map(int,input().split()))
    s={}
    b=set()
    for i in range(n-1):
        x,y=map(int,input().split())
        addEdge(x,y)
        b.add((x,y))
    bfs(1)
    b2=b.copy()
    for x,y in b:
        if x not in s:
            s[x]=np.array([a[x-1] for x in path[x]])
        if y not in s:
            s[y]=np.array([a[y-1] for y in path[y]])
    
    for i in range(q):
        p,r=map(int,input().split())
        #print(u,v)
        ans=sum(s[p]*s[r]) + a[p-1]*a[r-1]
        print(ans % 2**32)


