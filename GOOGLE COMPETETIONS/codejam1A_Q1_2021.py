for t in range(int(input())):
    n=int(input())
    a=[str(10**9)]*n
    print(a)
    ans=0
    for i in range(1,n):
        if int(a[i])<=int(a[i-1]):
            temp=str(int(a[i-1][-1])+(1))
            if temp=='10':
                temp='0'
            if i==n-1:
                if int(a[i]+temp*(abs(len(a[i]) - len(a[i-1]))))<=int(a[i-1]):
                    ans+=abs(len(a[i]) - len(a[i-1])) + 1
                    a[i]+=temp*(abs(len(a[i]) - len(a[i-1]))+1)
                else:
                    ans+=abs(len(a[i]) - len(a[i-1])) 
                    a[i]+=temp*(abs(len(a[i]) - len(a[i-1])))

            else:
                if int(a[i]+temp*(abs(len(a[i]) - len(a[i-1]))))<=int(a[i-1]):   
                    ans+=abs(len(a[i]) - len(a[i-1])) + 1
                    if len(a[i+1])==len(a[i]+temp*(abs(len(a[i]) - len(a[i-1]))+1)) and a[i+1][-1]!=temp:
                        if int(a[i]+temp*(abs(len(a[i]) - len(a[i-1]))+1))>=int(a[i+1]):
                            a[i]+=str(int(a[i+1][-1])-1)
                        else:
                            a[i]+=temp*(abs(len(a[i]) - len(a[i-1]))+1)
                    else:
                        a[i]+=temp*(abs(len(a[i]) - len(a[i-1]))+1)
                else:
                    ans+=abs(len(a[i]) - len(a[i-1])) 
                    if len(a[i+1])==len(a[i]+temp*(abs(len(a[i]) - len(a[i-1])))) and a[i+1][-1]!='0':
                        if int(a[i]+temp*(abs(len(a[i]) - len(a[i-1]))))>=int(a[i+1]):
                            a[i]+=str(int(a[i+1][-1])-1)
                        else:
                            a[i]+=temp*(abs(len(a[i]) - len(a[i-1])))
                    else:
                        a[i]+=temp*(abs(len(a[i]) - len(a[i-1])))
    print(a)
    print("Case #"+str(t+1)+": "+str(abs(ans)))
        