#include<stdio.h>
#include<math.h>
long long int min(long long int x, long long int y, long long int z)
 {
    long long int min = 1000000000000;
                if (x < min)
                min=x;
                if (y < min)
                min=y;
                if(z < min)
                min=z;
                return min;
}
int main()
{
    long long int n=0,a=0,b=0,c=0,ans=0;
    scanf("%lld%lld%lld%lld",&n,&a,&b,&c);

        if(n%4==0)
        printf("0\n");

        else if(n%4==1)
             printf("%lld\n",min(3*a,a+b,c));

        else if(n%4==2)
        {
            ans=min(2*a,2*c,b);
            for(int i=2;i<100000;i=i*2)
            {
                if(i*c>ans)
                    break;
                else
                ans=min(ans,i*c,i*c);
            }
            printf("%lld\n",ans);
        }

        else if(n%4==3)
        {
            ans=min(a,3*c,b+c);
            for(int i=3;i<100000;i=i+4)
             {
                if(i*c>a)
                    break;
                else
                ans=min(ans,i*c,i*c);
            }
            printf("%lld\n",ans);
        }
}
