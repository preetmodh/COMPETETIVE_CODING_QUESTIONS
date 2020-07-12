#include<stdio.h>
#include<math.h>
int main()
{
    int n=0,sum1=0,sum2=0,ans=0;
    scanf("%d\n",&n);

    int arr[n][n];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }
     for(int i=0,j=n-1;i<n;i++)
    {

               sum1=sum1 + arr[i][i];
               sum2=sum2 + arr[i][j-i];
    }
                ans=abs(sum1 - sum2);

                printf("%d\n",ans);
}
