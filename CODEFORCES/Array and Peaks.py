for t in range(int(input())):
    n,k=map(int,input().split())
    i=1
    a=list(range(1,n+1))
    while(i<n-1):
        if k==0:
            break
        a[i+1],a[i]=a[i],a[i+1]
        i+=2
        k-=1
    if k==0:
        print(*a)
    else:
        print(-1)


    