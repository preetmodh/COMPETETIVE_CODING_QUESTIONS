#include<stdio.h>
int main()
{
    long long int n=0;
    scanf("%lld",&n);

    long long int arr[n],ans=0;
    for(int i=0;i<n;i++)
    {
        scanf("%lld",&arr[i]);
    }
    for(int i=0;i<n;i++)
    {
        ans=ans + arr[i];
    }
    printf("%lld\n",ans);

}
