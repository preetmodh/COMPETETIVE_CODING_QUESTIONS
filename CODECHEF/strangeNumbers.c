#include<stdio.h>
#include<math.h>

int main()
{
    int T=0;
    scanf("%d",&T);
    for (int t=0;t<T;t++)
    {
        int x=0,k=0;
        scanf("%d%d",&x,&k);


            if (x<=k)
            {
            printf("0\n");
            }
             else if(k==1)
            {
            printf("1\n");
            }
            else if(k==2&&x==4)
            {
                printf("1\n");
            }
                else
                {
                     printf("0\n");
                }




    }
}
