#include<stdio.h>
void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
int main()
{
int T=0;
scanf("%d",&T);
for(int t=0;t<T;t++)
    {
        int n=0,m=0,x=0,y=0,count=0;
        scanf("%d%d",&n,&m);
        int arr[2][n+1];
        arr[0][0]=0;
        arr[1][0]=0;
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&arr[0][i]);
            arr[1][i]=i;
        }
        for(int i=0;i<m;i++)
        {
            scanf("%d%d",&x,&y);

                if(arr[0][x]!=arr[1][x]||arr[0][y]!=arr[1][y])
                {
                    if((arr[0][x]==arr[1][y])||(arr[0][y]==arr[1][x]))
                    {
                        swap(&arr[0][x],&arr[0][y]);
                    }
                }
        }

            for(int j=1;j<=n;j++)
            {
                if(arr[0][j]!=arr[1][j])
                {
                    swap(&arr[0][arr[0][j]],&arr[0][j]);
                    count++;
                    j=1;
                }
        }
        printf("%d\n",count);
    }
}
