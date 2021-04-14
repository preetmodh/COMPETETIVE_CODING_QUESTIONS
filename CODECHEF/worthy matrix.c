	#include<stdio.h>
	void createTable(long long int n,long long int m,long long int mtrx[n+1][m+1],
		long long int k, long long int p, long long int dp[n+1][m+1])
	{
		dp[1][1] = mtrx[1][1];
		for ( int j = 1; j < m+1; j++) {
			dp[1][j] = mtrx[1][j] +
					dp[1][j - 1];
		}
		for ( int i = 1; i < n+1; i++) {
			dp[i][1] = mtrx[i][1] +
					dp[i - 1][1];
		}
		for ( int i = 1; i < n+1; i++) {
			for ( int j = 1; j < m+1; j++) {
				dp[i][j] = mtrx[i][j] +
				dp[i - 1][j] + dp[i][j - 1] -
							dp[i - 1][j - 1];
			}
		}
	}
	 int countSubMatrixUtil(long long int n,long long int m,long long int a[n+1][m+1],long long int dp[n+1][m+1],
							long long int v, long long int p)
	{



		int count = 0;
		long long int subMatSum = 0;
		int j=m;
		for (long long int k=1;k<n+1;k++){
		for (int i = k ; i < n+1; i++) {

                long long int x= i -k +1;
                long long int y= j -k +1;

					subMatSum = dp[i][j] - dp[x-1][j] -
						dp[i][y-1] + dp[x-1][y-1];

				if (subMatSum/(k*k) < p) {
					continue;
				}
				else{
                    int start=k;
                    int end = m;
                    int ans = 0;
					while(start<=end){
						int mid=(start + end)/2;
                        int x= i -k +1;
                        int y= mid -k +1;

					subMatSum = dp[i][mid] - dp[x-1][mid] -
						dp[i][y-1] + dp[x-1][y-1];

					if(subMatSum/(k*k) >= p){
						ans=mid;
						end=mid-1;
					}
					else{
						start=mid+1;
					}
					}
					count+=(m - ans + 1);
				}
		}
		}
		return count;
	}
	long long int countSubMatrix(long long int n,long long int m,long long int mtrx[n][m], long long int k, long long int p)
	{
		long long int dp[n+1][m+1];
		for ( int i = 0; i < n+1; i++) {
			for ( int j = 0; j < m+1; j++) {
				dp[i][j] = 0;
			}
		}
		createTable(n,m,mtrx,k,p,dp);
		return countSubMatrixUtil(n,m,mtrx,dp,k, p);
	}
	// Driver Code
	int main()
	{
		int T=0;
		scanf("%d",&T);
	for(int t=0;t<T;t++){
		long long int n=0,m=0,k=0,s=0;
		scanf("%lld%lld%lld",&n,&m,&k);
		long long int a[n+1][m+1];
		for( int i=0; i<=n; i++) {
		  a[i][0]=0;
	   }
	   for( int j=0; j<=m; j++) {
		  a[0][j]=0;
	   }
		for( int i=1; i<=n; i++) {
		  for(int j=1;j<=m;j++) {

			 scanf("%lld", &a[i][j]);
		  }
	   }


		s=countSubMatrix(n,m,a,0,k);

	   printf("%lld\n",s);
	}
		return 0;
	}
