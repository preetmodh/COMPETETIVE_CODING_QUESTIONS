#include<stdio.h>
int main()
{
    int T=0;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
        int n=0,max=0;
        scanf("%d",&n);

        int arr[n];

        for(int i=0;i<n;i++)
            {
                scanf("%d",&arr[i]);

                if(arr[i]>max)
                {
                    max=arr[i];
                }

            }
         printf("%d\n",max);
    }
}
