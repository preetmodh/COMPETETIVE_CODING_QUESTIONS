for _ in range(int(input())):
    n=int(input())
    count=1
    for i in range(1,n+1):
        if i%2==0:
            count+=1
        else:
            count*=2
    print(count)
        
