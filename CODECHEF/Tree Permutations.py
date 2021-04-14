from collections import defaultdict
""" 

1
6 2
1 2
1 3
2 4
3 5
3 6
10 20 30 40 50 60
10 40 50 20 30 60

{1: {2: {}, 3: {}}, 2: {4: {}}, 3: {5: {}, 6: {}}}
"""
def tree(): return defaultdict(tree)
def dicts(t): return {k: dicts(t[k]) for k in t}

    
def myprint(d,a):
    for k, v in d.items():
        if isinstance(v, dict):
            print(k,end=' ')
            if k in a:
                myprint(a[k],a)
    print()
    
    
        
for t in range(int(input())):
    n,s=map(int,input().split())
    e=[]
    for i in range(n-1):
        x,y=map(int,input().split())
        x=x
        y=y
        e.append((x,y))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    paths=tree()
    for x,y in e:
        paths[x][y]
    a=dicts(paths)
    i=1
    s=' '
    myprint(a[1],a)
    print(s)

    



