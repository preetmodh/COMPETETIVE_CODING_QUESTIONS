for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    asum=sum(a)
    bsum=sum(b)
    flag=0
    cnt=0
    for i in range(min(len(a),len(b))):
        if asum>bsum:
            break
        else:
            asum = asum - a[i] + b[i]
            bsum = bsum - b[i] + a[i]
            cnt+=1
    if asum>bsum:
        print(cnt)
    else:
        print(-1)
    
