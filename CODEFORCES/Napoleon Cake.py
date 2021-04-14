for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.reverse()
    l=[0]*n
    for i in range(len(a)):
        if a[i]==0:
            continue
        else:
            for j in range(1,a[i]+1):
                if (len(a)-i)-j>=0:
                    l[(len(a)-i)-j]=1
    print(*l)