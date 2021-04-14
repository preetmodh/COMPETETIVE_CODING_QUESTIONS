import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    if n%2==0:
        if n%4==0:
            print(n//4,n//4,( n - 2*(n//4)))
        else:
            print(n//2-1,n//2-1,( n - 2*(n//2-1)))
    else:
        print((n-1)//2,(n-1)//2,1)