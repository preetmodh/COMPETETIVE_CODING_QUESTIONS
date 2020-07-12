#include<stdio.h>
int main()
{
long long int n=0;
scanf(" %lld",&n);
long long int l=1,r=n,m1=0,m2=0;
m1=(l+r)/2;
m2=(l+r)/2 + 1;
char ans;

while(1)
{
printf("%lld\n",m1);
scanf(" %c",&ans);
if(ans=='E')
{return 0;}

printf("%lld\n",m1);
scanf(" %c",&ans);
if(ans=='E')
{return 0;}


if(ans=='L')
{

    r=m1;
}


printf("%lld\n",m2);
scanf(" %c",&ans);
if(ans=='E')
{return 0;}

printf("%lld\n",m2);
scanf(" %c",&ans);
if(ans=='E')
{return 0;}

if(ans=='G')
{
    l=m2;

}
m1=(l+r)/2;
m2=(l+r)/2 + 1;
}
}
