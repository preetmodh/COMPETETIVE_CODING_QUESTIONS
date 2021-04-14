for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    if n%2!=0:
        s=s[0:n//2] + s[n//2:len(s)]
    cnt=0
    for i in range(len(s)//2):
        if s[i]!=s[(len(s)-1) - i]:
            #print(s[i],s[(len(s)-1) - i])
            cnt+=1
    print("Case #"+str(_+1)+": "+str(abs(k-cnt)))