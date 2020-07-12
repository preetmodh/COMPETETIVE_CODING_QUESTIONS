#include<stdio.h>

void compareTwo(int ac[] ,int bc[])
{
    int sumA=0,sumB=0;
    int ans[2];
    for(int i=0;i<3;i++)
    {
        if(ac[i]>bc[i])
        sumA++;

        else if(ac[i]<bc[i])
        sumB++;

        else
        continue;
    }
        ans[0]=sumA;
        ans[1]=sumB;

        for(int i=0;i<2;i++)
        {
            printf("%d ",ans[i]);
        }

}

int main()
{
    int a[3],b[3];

    for(int i=0;i<3;i++)
    {
        scanf("%d",&a[i]);
    }
    for(int i=0;i<3;i++)
    {
        scanf("%d",&b[i]);
    }

        compareTwo(a,b);

}
