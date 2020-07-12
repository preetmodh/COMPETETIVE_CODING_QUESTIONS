#include<stdio.h>
#include<math.h>
int main()
{
    int t=0;
    scanf("%d",&t);
    for (int m=0;m<t;m++)
    {
        int n=0;
        scanf("%d",&n);
        for(int i=1;i<=n*n;i++)
        {
            printf("%d ",i);
            if(i%n==0)
                printf("\n");
        }
    }
}
