#include<stdio.h>
int main()
{
    int n=0;
    scanf("%d",&n);
    for(int i=1;i<=10;i++)
        printf("%d x %d = %d\n",n,i,n*i);
}
