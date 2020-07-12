#include<stdio.h>
#include<time.h>
int main()
{

    int T=0;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
        int n=0,k=0,count=0,i;
        scanf("%d%d",&n,&k);
        int array[n];
        for(i=0;i<n;i++)
                scanf("%d",&array[i]);

        if(n%4==2||n%4==3)
            printf("-1\n");

        else
            {
               printf("%d\n",n/2);
               for(i=0;i<n;i=i+2)
                {
                    int j=n - i;
                    printf("%d %d %d\n%d %d %d\n",i+1,j-1,j,i+2,j-1,j);
                     count=count+2;
                     if(count==n/2)
                         break;
                }
            }
    }
}
