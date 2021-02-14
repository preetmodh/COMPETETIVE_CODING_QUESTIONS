from collections import Counter 
for _ in range(int(input())):
    n,q,m=map(int,input().split())
    a=list(map(int,input().split()))
    s=[]
    for Q in range(q):
        l,r=map(int,input().split())
        s.append((l-1,r-1))
    cnt=0
    for g in range(1,m+1):
        w=0
        for l,r in s:
            if a[l]>g or a[l]>m:
                continue
            lv=a[l]
            rv=a[r] + lv
            while(True):
                if lv<=g and rv>g:
                    w+=1
                    break
                if lv>g or lv>m:
                    break

                lv=rv+a[l]
                rv=lv+a[r]
        cnt=max(cnt,w)
    print(cnt)

        
