#include<stdio.h>
#include<math.h>
long long int min(long long int a,long long int b)
{
    if(a>b)
    return b;
    else
    return a;
}
int main()
{
	int T=0;
	scanf("%d",&T);
for(int t=0;t<T;t++)
{
   long long int x,y,l,r,z=0,temp=0,ans=0,count=0,l2=0;
   scanf("%lld%lld%lld%lld",&x,&y,&l,&r);
        temp=r;
            while(temp>0)
                {
                    temp=temp/2;
                    count++;
                }

if(x==0 || y==0)
    z=0;
else if(((x|y)>=l) && ((x|y)<=r))
        z=x | y;
else if(r==l)
        z=r;
else
    {
        if(l<pow(2,count-1))
       {
           l=pow(2,count-1);
                if(r==l)
                {
                    l=pow(2,count-2);
                }
       }
        l2=l;
       if((x|y)%2==1)
       {
           l=l+1;
       }
        for(int i=0;i<min(32,r);i=i+1)
            {
                temp=(i&x)*(i&y);
                //printf("%d %d\n",i,temp);
                    if(ans<temp)
                        {
                            ans=temp;
                            z=i;
                        }
            }


            if(r>=(l2+z)&&r>32)
            {
                z=l2+z;
                ans=(z&x)*(z&y);
            }
			else if(r<(l2+z)&&r>32)
			{
			     long long int z2=l2/2+z;
                 long long int temp2=(z2&x)*(z2&y);
                    for(int i=l2;i<=r;i++)
                    {
                        temp=(i&x)*(i&y);
                        if(ans<temp)
                            {
                                ans=temp;
                                z=i;
                            }
                    }
                    if(temp2>ans)
                        {
                            z=z2;
                        }
			}
            temp=(r&x)*(r&y);
            if(ans<temp)
                        {
                            ans=temp;
                            z=r;
                        }
    }
            printf("%lld\n",z);
	}
}
