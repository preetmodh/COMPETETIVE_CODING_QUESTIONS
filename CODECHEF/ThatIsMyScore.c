#include<stdio.h>
int main()
{
    int t,n,que,score,max;

    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%d",&n);


        int arr[12];
        max=0;

        for(int j=0;j<n;j++)
        {
            scanf("%d %d",&que,&score);

            if(que>0&&que<9)
                {
                    if(arr[que]<=score)
                    {
                    arr[que]=score;
                    }
                }

        }
                for( int p=1;p<9;p++)
                {
                    {
                    max=max + arr[p];
                    }
                }
            printf("%d\n",max);
    }

}
