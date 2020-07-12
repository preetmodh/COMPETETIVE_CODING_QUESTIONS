#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
	int n=0,f=0,k=0;
	scanf("%d %d",&n,&f);
	int arr[n][n];
	for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            scanf("%d",&arr[i][j]);
        }
    }
    scanf("%d",&k);
    char str[]={'L','U','R','D'};

            printf("%d\n",k-1);
    for(int i=1;i<=k-1;i++)
    {
        if(i<n)
        {
            printf("%c %d\n",str[0],i);
            printf("%c %d\n",str[1],i);
        }
        else
        {
            printf("%c %d\n",str[2],i);
            printf("%c %d\n",str[3],i);
        }

    }
    return 0;

}

