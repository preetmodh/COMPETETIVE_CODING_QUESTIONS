#include<stdio.h>
#include<math.h>
int main()
{
    int T=0;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
        int n=0,count=0,hold=0;
        scanf("%d",&n);
        int arr[n];
        for(int i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
            hold=arr[0];
            if(abs(arr[i]-hold)%2==0)
                count++;
        }
        if(count==n)
            printf("YES\n");
            else
                printf("NO\n");
    }
}
