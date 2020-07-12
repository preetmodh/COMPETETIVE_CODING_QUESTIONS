#include<stdio.h>
int main()
{
    int T=0;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
        int n=0,q=0,a=0;
        scanf("%d%d",&n,&q);
        int Y[n],X[n];
        for(int i=0;i<n;i++)
            scanf("%d",&Y[i]);

        for(int i=1;i<=n;i++)
            {
                X[a]=i;
                a++;
            }

        for(int i=0;i<q;i++)
            {

                        int count=0;
                        int x1=0, y=0, x2=0;

                        scanf("%d%d%d",&x1,&x2,&y);

                        /*for(int j=x1;j<x2;j++)
                        {


                                if ((y>=Y[j-1]&&y<=Y[j])||(y<=Y[j-1]&&y>=Y[j]))
                                count++;


                        }*/

                        float slope=0,intercept=0,x=0;




                        for(int j=1;j<n;j++)
                        {
                            if(j>=x1&&j<x2)
                            {
                                slope=(Y[j-1]-Y[j])/(X[j-1]-X[j]);

                            if(((X[j-1]==x2)&&(Y[j-1]==y))||((X[j]==x1)&&(Y[j]==y)))
                                continue;


                                if((slope==0)&&(Y[j]==y))
                                  {
                                      if((X[j-1]<x2&&X[j]>=x2)&&(X[j-1]<=x1&&X[j]>x1))
                                      {
                                          count++;
                                      }
                                       else if((X[j-1]<x2&&X[j]>=x2)&&(X[j-1]>=x1))
                                       {
                                           count++;
                                       }
                                       else if((X[j-1]<=x1&&X[j]>x1)&&(X[j]<=x2))
                                       {
                                           count++;
                                       }
                                  }


                            else
                            {
                                intercept=Y[j-1] - (slope * X[j-1]);
                                x=(y-intercept)/slope;



                                if((x>=X[j-1]&&x<=X[j])&&(x>=x1&&x<=x2))
                                {
                                count++;
                                }

                            }
                            }
                        }






                            printf("%d\n",count);

            }
    }
}
