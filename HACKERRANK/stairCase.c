#include<stdio.h>

int main()
{
    int n=0,count=0;
    scanf("%d",&n);

    count=n-1;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=count;j++)
        {
            printf(" ");
        }
        for(int k=1;k<=i;k++)
            printf("#");

        printf("\n");
        count--;
    }
}
