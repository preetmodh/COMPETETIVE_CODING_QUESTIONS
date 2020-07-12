#include<stdio.h>
int main()
{
    int T=0;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
        int n=0;
        scanf("%d",&n);
        long long int arr[n],arr1[n];
        for(int i=0;i<n;i++)
        {
            scanf("%lld",&arr[i]);
            arr1[i]=0;
        }
        for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(arr[i]>arr[j])
            {
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
    if(n%2!=0)
    {       arr1[n-1]=arr[n/2];
            int k=n/2;
            int p=0;

        for(int j=0;j<k;j=j+1)
            {
               arr1[p]=arr[j];
               p=p+2;
            }
                p=1;
        for(int j=n-1;j>k;j=j-1)
            {
               arr1[p]=arr[j];
               p=p+2;
            }
    }
    else
        {
            int k=n/2 - 1;
            int p=0;

        for(int j=0;j<=k;j=j+1)
            {
               arr1[p]=arr[j];
               p=p+2;
            }
                p=1;
        for(int j=n-1;j>=k;j=j-1)
            {
               arr1[p]=arr[j];
               p=p+2;
            }
        }

    for(int i=n-1;i>=0;i--)
        printf("%lld ",arr1[i]);

    }
}
