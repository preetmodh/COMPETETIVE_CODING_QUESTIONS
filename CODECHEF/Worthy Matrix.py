def createTable(mtrx, k, p, dp,n,m):
    dp[0][0] = mtrx[0][0]
    
    for j in range(1, m):
        dp[0][j] = mtrx[0][j] + dp[0][j - 1]

    for i in range(1, n):
        dp[i][0] = mtrx[i][0] + dp[i - 1][0]
    
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = (mtrx[i][j] +
                        dp[i - 1][j] +
                        dp[i][j - 1] -
                        dp[i - 1][j - 1])
def countSubMatrixUtil(a,dp, v, p,n,m):
    
    count = 0
    subMatSum = 0
    for k in range(1,n+1):
        avg=k*k*p
        for i in range(k-1, n):
            j=m-1
            if (i == (k - 1) or j == (k - 1)):
                
                if (i == (k - 1) and j == (k - 1)):
                    subMatSum = dp[i][j]
                    
                elif (i == (k - 1)):
                    subMatSum = dp[i][j] - dp[i][j - k]
                    
                else:
                    subMatSum = dp[i][j] - dp[i - k][j]
                    
            else:
                subMatSum = (dp[i][j] -
                            dp[i - k][j] -
                            dp[i][j - k] +
                            dp[i - k][j - k])

            if subMatSum<avg:
                continue
            else:
                start=k-1
                end=m-1
                ans=0
                while (start<=end):
                    j=(start+end)//2
                    if (i == (k - 1) or j == (k - 1)):
                        
                        if (i == (k - 1) and j == (k - 1)):
                            subMatSum = dp[i][j]
                            
                        elif (i == (k - 1)):
                            subMatSum = dp[i][j] - dp[i][j - k]
                            
                        else:
                            subMatSum = dp[i][j] - dp[i - k][j]
                            
                    else:
                        subMatSum = (dp[i][j] -
                                    dp[i - k][j] -
                                    dp[i][j - k] +
                                    dp[i - k][j - k])

                    if subMatSum>=avg:
                        ans=j
                        end=j-1
                    else:
                        start=j+1
                count+=(m - ans)

    return count
    
def countSubMatrix(mtrx, k, p,n,m):
    
    dp = [[0 for i in range(m)]
            for j in range(n)]
    
    
    for i in range(n):
        for j in range(m):
            dp[i][j] = 0
    
    createTable(mtrx, k, p, dp,n,m)
    #print(dp)
    return countSubMatrixUtil(mtrx,dp, k, p,n,m)



for t in range(int(input())):
    n,m,k=map(int,input().split())
    a=[]
    s=0
    for i in range(n):
        a.append(list(map(int,input().split())))
    if n==1 and m==1:
        if a[0][0]>=k:
            print(1)
        else:
            print(0)
        continue

    
    s=countSubMatrix(a, 0,k,n,m)
    print(s)
