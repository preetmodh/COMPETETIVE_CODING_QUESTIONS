#include<stdio.h>
#include<stdlib.h>
int main()
{
            int a[100000],n=0,count=0,index=0,ans=0;

            scanf("%d",&n);

                for(int i=0;n>0;i++)
                    {
                        a[i]=n%2;
                        n=n/2;
                        index++;

                    }

                for(int i=0;i<index;i++)
                    {

                       if(a[i]==0)
                        count=0;

                       else
                       {
                           count++;
                           ans=(ans > count ) ? ans : count;

                       }

                    }
                                printf("%d",ans);
                                return 0;
}

