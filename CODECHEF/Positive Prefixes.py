for _ in range(int(input())):
    n,k=map(int,input().split())
    k=n-k
    a=list(range(1,n+1))
    cnt=0
    for i in range(len(a)):
        if a[i]%2!=0:
            if cnt<k:
                a[i]=-a[i]
                cnt+=1
            else:break
    a.reverse()
    for i in range((len(a))):
        if a[i]%2==0:
            if cnt<k:
                a[i]=-a[i]
                cnt+=1
            else:break
    print(' '.join(map(str,reversed(a))))