#include<stdio.h>
unsigned long long int factorial(unsigned long long int n)
{
    if(n==1)
    return 1;

    else
    return n*factorial(n-1);
}
int main()
{
    unsigned long long int N=0;
    scanf("%llu",&N);
    printf("%llu",factorial(N));
}
