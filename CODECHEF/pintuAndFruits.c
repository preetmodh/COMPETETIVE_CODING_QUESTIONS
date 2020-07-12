#include<stdio.h>

int main()
{
    int T=0;
    scanf("%d",&T);

        for(int t=0;t<T;t++)
        {
            int n=0,m=0;
            scanf("%d%d",&n,&m);

            int arr[2][n],bul[m+1],sum[m+1];
            for(int i=0;i<2;i++)
            {
                for(int j=0;j<n;j++)
                {
                    scanf("%d",&arr[i][j]);
                }
            }
                for(int j=0;j<m+1;j++)  //initializing all bul elements to zero
                    {
                        bul[j]=0;
                    }
                for(int j=0;j<n;j++)
                    {
                    bul[arr[0][j]]=1;    //setting only values of arr elements numbers to 1 in bul
                    }

                for(int j=0;j<m+1;j++)  //initializing all sum elements to zero
                    {
                        sum[j]=0;
                    }

            for(int i=0;i<n;i++)
            {

                    sum[arr[0][i]]=sum[arr[0][i]] + arr[1][i];  // for summing

            }

                int min=10000;
            for(int i=1;i<=m;i++)
            {
                if(bul[i]==1)      // if the values of bul is equal to one and sum<max
                {
                    if (sum[i]<min)
                     min=sum[i];
                }
            }

            printf("%d\n",min);

        }

}

