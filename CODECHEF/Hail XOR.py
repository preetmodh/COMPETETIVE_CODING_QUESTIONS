import math 
def powerof2(n): 
    p = int(math.log(n, 2)); 
    return int(pow(2, p));  

for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    cnt=0
    i=0
    while(True):
        if i>=n-1:
            if cnt>=x:
                break
            else:
                num=x-cnt
                if n==2 and num%2!=0:
                    a[-2]=a[-2] ^ 1
                    a[-1]=a[-1] ^ 1
                break
        if a[i]!=0:
            p=powerof2(a[i])
            a[i]=a[i] ^ p
            flag=1
            for j in range(i+1,n):
                if a[j]^p < a[j]:
                    a[j]=a[j] ^ p
                    cnt+=1
                    flag=0
                    break
            if flag==1:
                a[-1]=a[-1] ^ p
                cnt+=1
            if cnt>=x:
                break
        if a[i]==0:
            i+=1
    print(' '.join(map(str,a)))


