#include<stdio.h>
int countBits(int a)
{
    //base case
    if(a==0)
        return 0;

    // if last bit set add 1 else add 0
    else
        return (a & 1) + countBits(a >> 1);
}
int main()
{
    int T=0;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
        int n=0,q=0,m=0;
        scanf("%d%d",&n,&q);

        int arr[n],p[q],count=0;
        for(int i=0;i<n;i++)
            scanf("%d",&arr[i]);

         for(int i=0;i<q;i++)
        {
            scanf("%d",&p[i]);
            int store[n],c[n];
             int value=0,even=0,odd=0;

            for(int j=0;j<n;j++)
            {
                store[j]=p[i]^arr[j];
                c[j]=countBits(store[j]);

            }

            /*for(int j=0;j<n;j++)
                    {
                        count=0;
                        m=store[j];
                        for(;m>0;)
                            {
                                value=m%2;
                                if(value==1)
                                    {
                                    count++;
                                    }
                            m=m/2;
                            }
                            c[j]=count;
                    }*/
                    for (int j=0;j<n;j++)
                    {
                        if(c[j]%2==0)
                            even ++;

                        else
                            odd++;
                    }
                    printf("%d %d\n",even,odd);

        }

    }
}
