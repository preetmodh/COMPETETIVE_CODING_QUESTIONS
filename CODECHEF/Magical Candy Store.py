MOD = 1000000007
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    q=int(input())
    s=set()
    if n!=1:
        if a[0]==1:
            pass
        elif (a[-1]==1) or (1 not in a):
            for i in range(len(a)-1):
                if a[i]%2!=0:
                    a[i]=a[i]-1
                    s.add(i)
            if a[-1]%2==0:
                a[-1]=a[-1] - 1
                s.add(n-1)
            else:
                pass
        else:
            ind=-1
            for i in range(len(a)-1):
                if a[i]==1:
                    ind=i
                if a[i]%2!=0:
                    s.add(i)
                    a[i]-=1
            if ((ind-1) not in s):
                a[ind-1]=a[ind-1] - 1
                s.add(ind-1)
            else:
                a[ind-1]=a[ind-1] + 1
                s.remove(ind-1)
                s.remove(ind)
            if a[-1]%2==0:
                a[-1]-=1
                s.add(n-1)
            else:
                pass
    b=a.copy()
    for i in range(1,len(b)):
        b[i]=b[i-1]+b[i]

    for x in range(q):
        r=int(input())
        if n==1:
            if a[0]%2!=0:
                print(( ( r % MOD ) * ( a[n-1] % MOD ) ) % MOD)
            else:
                ans=( ( r % MOD ) * ( (a[n-1]-1) % MOD ) ) % MOD
                print((( ans % MOD )+( 1 % MOD )) % MOD) 

        else:
            if a[0]==1:
                ans=0
                if (r%n==0 or r%n==1) and r!=1:
                    ans=r//n
                else:
                    ans=r//n + 1
                print(ans % MOD)
            else:
                mul=r//n
                sum = 0
                sum =(( sum % MOD ) + ( b[-1]*mul % MOD )) % MOD
                i=r%n
                if i==0:
                    i=n-1
                else:
                    sum = sum + b[i-1]
                    i=i-1

                if (i in s):
                    sum+=1
                    if (i-1) in s and a[i]==0:
                        sum+=1          
                print(sum % MOD)