#include<stdio.h>

int main()
{
   int T;
   int Thits;
   scanf("%d",&T);
   for(int i=0;i<T;i++)
   {
                    int S,W1,W2,W3;
                    scanf("%d%d%d%d",&S,&W1,&W2,&W3);
                    int W=W1+W2+W3;
                    if (S>=W)
                        {
                        Thits=1;
                        }
                    else if((S>=W1+W2) ||(S>=W2+W3))
                        {
                        Thits=2;
                        }
                    else
                        {
                        Thits=3;
                        }
                        printf("%d\n",Thits);
   }
}
