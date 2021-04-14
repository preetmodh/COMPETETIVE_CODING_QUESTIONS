MAX=10**6
dp=[0]*(MAX+2)
dp1=[0]*(MAX+2)
arr0=[0]*(MAX)
arr1=[0]*(MAX)

def solve(s):
    n=len(s)
    lp=-1
    for i in range(n):
        if s[i]=='0':
            for j in range(lp+1,i+1):
                arr0[j]=i
            lp=i
    for  i in range(lp+1,n):
        arr0[i]=n
    
    if arr0[0]==n:
        print(0)
        return None
    
    lp=-1
    for i in range(n):
        if s[i]=='1':
            for j in range(lp+1,i+1):
                arr1[j]=i
            lp=i
    for  i in range(lp+1,n):
        arr1[i]=n

    dp[n],dp[n+1]=0,0
    dp1[n],dp1[n+1]=0,0

    for i in range(n-1,-1,-1):
        dp[i]=dp[i+1]
        if s[i]=='0' and arr1[i]<n:
            dp[i]=max(dp[i],dp[arr1[i] + 1] + 1)
        if s[i]=='1' and arr0[i]<n:
            dp[i]=max(dp[i],dp[arr0[i] + 1] + 1)
        dp1[i]=dp1[i+1]
        if arr1[i]<n:
            dp1[i] = max(dp1[i],dp[arr1[i]+1] + 1)
    

    length=dp1[0]+1
    ind=arr1[0]+1
    ans="1"
    for i in range(1,length):
        if ind>=n:
            ans+="0"
            continue
        if arr0[ind]>=n:
            ans+="0"
            ind=arr0[ind] + 1
            continue
        if (dp[arr0[ind] + 1] < length - i - 1): 
            ans+='0'
            ind = arr0[ind] + 1
        else :
            ans+='1'
            ind = arr1[ind] + 1
    print(ans)
    

for t in range(int(input())):
    s=input()
    solve(s)
    
    