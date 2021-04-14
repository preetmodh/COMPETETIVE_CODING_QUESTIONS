for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(len(a)-1):
        #print(a[i])
        #print(a)
        m=min(a[i:len(a)])
        
        #print("m "+str(m))
        ind=a.index(m)+1
        #print("i "+str(ind))
        if a[i]==m:
            ans+=1
        else:
            ans+=ind - i
            a[i:ind]=reversed(a[i:ind])
        #print("ans "+str(ans))
    print("Case #"+str(t+1)+": "+str(abs(ans)))













