#include<stdio.h>
#include<math.h>

int main(void)
{               int T;
                scanf("%d",&T);

               for(int i=0;i<T;i++)
               {

                int N, A, B, C, D, P, Q, Y;
               scanf("%d %d %d %d %d %d %d %d", &N,&A,&B,&C,&D,&P,&Q,&Y);
               int arr[N];
               for(int j=1;j<=N;j++)
               {
                   scanf("%d",&arr[j]);
               }
                int Twalk=abs(arr[B]-arr[A]) * P;
                int G=abs(arr[C]-arr[A]) * P;
                int H=abs(arr[D]-arr[C]) * Q;
                int I=abs(arr[D]-arr[B]) * P;
                int Ttrain;

                if(G<=Y)
                {
                    Ttrain= Y + H + I;

                    if (Twalk>Ttrain)
                    {
                    printf("%d",Ttrain);
                    }
                     else
                        {
                     printf("%d",Twalk);
                        }
                }
                 else
                        {
                     printf("%d",Twalk);
                        }

                }return 0;
 }

