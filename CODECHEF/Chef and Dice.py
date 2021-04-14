for t in range(int(input())):
    n=int(input())
    a=[0,20,36,51,60]
    ans=0
    base=60
    m=n%4
    if n>4:
        ans=base + 44*(n//4 - 1) - 4*(m) + a[m]
    else:
        if m==0:
            m=4
        ans=a[m]
    print(ans)
    
