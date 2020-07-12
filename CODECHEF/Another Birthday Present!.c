#include<stdio.h>
int main()
{
    int T=0;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
        int n=0,k=0;
        scanf("%d%d",&n,&k);

        long long int arr[n];

        for(int i=0;i<n;i++)
            {
                scanf("%lld",&arr[i]);
            }

        for(int i=0;i<n;i++)
        {
            for(int j=i+k;j<n;j=j+k)
            {
                if(arr[i]>arr[j])
                {
                    long long  int temp=arr[i];
                                                arr[i]=arr[j];
                                                arr[j]=temp;
                }
            }
        }

        int bul=0;
         for(int i=0;i<n-1;i++)
         {
             if(arr[i]<=arr[i+1])
             {
                bul=1;
             }
             else
             {
                 bul=0;
                 break;
             }
         }
         if(bul==1)
         printf("yes\n");

         else
            printf("no\n");
    }
}
