#include<stdio.h>
int main()
{
    int arr[6][6];
    int sum[16];
    int count=0;
    for(int i=0;i<6;i++)
    {
        for(int j=0;j<6;j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }


    for(int i=0;i<4;i++)
    {
        for(int j=1;j<5;j++)
        {
            sum[count]=arr[i][j-1] + arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j-1] + arr[i+2][j] + arr[i+2][j+1];
            count++;
        }
    }


    for (int i = 0; i < 16; ++i)
        {
            for (int j = i + 1; j < 16; ++j)
            {
                if (sum[i] > sum[j])
                {
                    int temp =  sum[i];
                    sum[i]=sum[j];
                    sum[j] = temp;
                }
            }
        }
printf("%d",sum[15]);


}

