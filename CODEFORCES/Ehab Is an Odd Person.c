#include <stdio.h>
int main()
{
    int n=0;
    scanf("%d",&n);
    long long int array[n];
    for(int i=0;i<n;i++)
    {
        scanf("%lld",&array[i]);
    }
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(array[i]>array[j]&&((array[i]+array[j])%2!=0))
            {
                long long int temp=array[i];
                array[i]=array[j];
                array[j]=temp;
            }
        }
    }
    for(int i=0;i<n;i++)
    {
        printf("%lld ",array[i]);
    }

}
