def change(string):
    for i in range(len(string)):
            if string[i]=="?":
                if i==0:
                    string[i]=string[i+1]
                elif i==len(string)-1:
                    string[i]=string[len(string)-2]
                else:
                    string[i]=string[i-1]
            else:
                continue
    string=''.join(string)

    return string

testcase=int(input())
for t in range(testcase):
    a=input().split()
    X=int(a[0])
    Y=int(a[1])
    string=a[2]
    string=list(string)
    ans=0
    if len(string)==1:
        print("Case #"+str(t+1)+": "+str(abs(ans)))
    else:
        
        string =change(string)

        
        ans=X*string.count("CJ")
        ans+=Y*string.count("JC")

        print("Case #"+str(testcase+1)+": "+str(ans))