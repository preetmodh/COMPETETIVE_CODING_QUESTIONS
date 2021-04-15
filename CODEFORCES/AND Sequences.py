MOD=10**9 + 7
fac=[1]
for i in range(2*(10**5)):
    fac.append((fac[-1]*(i+1))%MOD)
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ands=a[0]
    put=0
    for i in range(1,n):
        temp=ands & a[i]
        if temp!=ands:
            put=-1
            break
    if a.count(a[0])<2 or put==-1:
        print(0)
        continue
    if len(set(a))==1:
        print((fac[n]%MOD)%MOD)
        continue
    else:
        x=a.count(a[0])
        ans=((x*(x-1)))%MOD
        ans=((ans%MOD)*(fac[n-2]%MOD))%MOD
        print(ans % MOD)




        
