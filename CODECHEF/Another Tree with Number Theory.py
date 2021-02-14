from collections import Counter
def recur(d,v,task,taskr):
    if v not in d:
        return 0
    elif task%len(d[v])!=0:
        return task
    else:
        for i in d[v]:
            taskr+=recur(d,i,task//len(d[v]),taskr)

    return taskr

n=int(input())
a=list(map(int,input().split()))
d=dict()
for i in range(0,n-1):
    if a[i] not in d:
        d[a[i]]=[i+2]
    else:
        d[a[i]]+=[i+2]
q=int(input())
for Q in range(q):
    v,w=map(int,input().split())
    an=0 
    ans=recur(d,v,w,an)
    print(ans)