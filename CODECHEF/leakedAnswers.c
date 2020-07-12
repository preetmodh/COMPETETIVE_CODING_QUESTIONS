#include<stdio.h>
int main ()
{
    int T=0;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
        int n=0,m=0,k=0;
        scanf("%d%d%d",&n,&m,&k);
        int arr[n][k];

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<k;j++)
            {
                scanf("%d",&arr[i][j]);
            }
        }

        for(int i=0;i<n;i++)
        {

            printf("%d ",arr[i][1]);

        }printf("\n");
    }
}
