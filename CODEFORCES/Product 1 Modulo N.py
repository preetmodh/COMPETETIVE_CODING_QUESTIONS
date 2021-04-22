
from math import gcd as gd

n=int(input())
a=[]
p=1
if n==2:
    print(1)
    print(1)
else:
    for i in range(1,n):
        if gd(i,n)==1:
            p=p*i % n
            if i==n-1 and p%n==n-1:
                pass
            else:
                a.append(i)
    print(len(a))
    print(' '.join(map(str,a)))
 
 
