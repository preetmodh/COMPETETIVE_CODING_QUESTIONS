#include<stdio.h>
#include<math.h>
int main()
{
    int T=0;
    scanf("%d",&T);
for(int t=0;t<T;t++)
{
    long long int p=1;
    int n=0,count=0;
    scanf("%d",&n);
    long long int arr[n];
     for(int i=0;i<n;i++)
     {
         scanf("%lld",&arr[i]);
     }
    for(int i=0;i<n;i++)
    {
        p=arr[i];
        if (abs(p)%4!=2)
            {
                count++;
            }
            for(int j=i+1;j<n;j++)
        {

                    p=p*arr[j];
                    if (abs(p)%4!=2)
                        {
                        count++;
                        }
        }
    }
    printf("%d\n",count);
}
}
