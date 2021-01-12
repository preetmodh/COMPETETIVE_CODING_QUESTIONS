for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    m=x.pop(0)
    cnt=0
    for i in x:
        if i<0:
            cnt+=1
    print(cnt*(len(x) - cnt))
