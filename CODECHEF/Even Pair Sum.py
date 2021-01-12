for _ in range(int(input())):
    a,b=map(int,input().split())
    odda,oddb,evena,evenb=a//2,b//2,a//2,b//2
    if a%2!=0:odda+=1
    if b%2!=0:oddb+=1
    print(odda*oddb + evena*evenb)