for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(set((a)))
    cnt=a.count(b[0])
    cnt2=a.count(b[1])
    if cnt<cnt2:
        print(a.index(b[0])+1)
    else:
        print(a.index(b[1])+1)