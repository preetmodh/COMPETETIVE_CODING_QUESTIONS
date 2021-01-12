for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if n==1 or sum(a)<(2*k):
        print(-1)
    else:
        s2=set()
        cnt=-1
        a.sort(reverse=True)
        sums=a[0]
        s2.add(a[0])
        sum1=0
        sum2=0
        if a[0]>=k and a[1]>=k:
            print(2)
        else:
            for i in range(1,n):
                sums=sums+a[i]
                for j in list(s2):
                    s2.add(a[i])
                    sum1=j + a[i]
                    sum2=sums - sum1
                    s2.add(sum1)
                    if sum1>=k and sum2>=k:
                        cnt = i + 1
                        break
                if cnt!=-1:
                    break
            print(cnt)

