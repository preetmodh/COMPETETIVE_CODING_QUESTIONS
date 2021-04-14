def Diff(a,b):
    l1=a.copy()
    l2=b.copy()
    l1.sort()
    l2.sort()
    diff=[]
    for i in range(len(l1)):
        if l1[0] in l2:
            ind=l2.index(l1[0])
            l2.pop(ind)
        else:
            diff.append(l1[0])
        l1.pop(0)
    return sorted(list(set(diff)))

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(list(set(a)))
    while(True):
        if len(Diff(a,b))==0:
            break
        else:
            temp = Diff(a,b)
            b = b + temp
    print(*b)

