#include<stdio.h>

int main()
{
    int T=0,S=0;
    scanf("%d%d",&T,&S);
    if(S==1)
    {
    for(int t=0;t<T;t++)
    {

            int n=0,check=0,helper=1,min=0;
            scanf("%d",&n);

            int a[n],b[n],c[n];
            char s[]="NO";
            for(int i=0;i<n;i++)
                {
                    scanf("%d",&a[i]);
                    if(i==0)
                        {
                            check=a[i];
                            min=a[i];
                        }
                        if(a[i]<min)
                            min=a[i];

                    if(check==a[i])
                        helper++;
                }

            for(int i=0;i<n;i++)
                {
                    scanf("%d",&b[i]);
                    if(b[i]==check)
                    helper++;
                }

                if(helper==2*n)
                    continue;

                else
                {   int bul=0;
                    for(int i=0;i<n;i++)
                        {
                            for(int j=0;j<n;j++)
                            {
                                if(a[i]==b[j])
                                    {
                                        c[bul]=b[j];
                                        bul++;
                                        break;
                                    }
                            }
                        }





                }









    }
    }
}
