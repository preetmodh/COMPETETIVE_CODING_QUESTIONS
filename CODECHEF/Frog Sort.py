for i in range(int(input())):
    n=int(input())
    w=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a=[]
    for i in range(n):
        a.append([i+1,w[i],b[i]])
    a.sort(key = lambda x: x[1])
    cnt=0
    for i in range(1,len(a)):
        if a[i-1][0]>=a[i][0]:
            while(a[i-1][0]>=a[i][0]):
                a[i][0]+=a[i][2]
                cnt+=1
    print(cnt)

