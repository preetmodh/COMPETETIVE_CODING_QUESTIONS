#include<stdio.h>
#include<math.h>

int main()
{
    int T;
   scanf("%d",&T);
   for(int i=0;i<T;i++)
    {
                    int N;
                    long long int A, S, B, C, D, E,Return;

            scanf("%d",&N);


                    long long int newN=(int)pow(10,N);

            scanf("%lld",&A);


            S=(newN * 5 - 1) +A;


            printf("%lld\n",S);
            fflush(stdout);

            scanf("%lld",&B);


            C=newN - B;
            printf("%lld\n",C);
            fflush(stdout);

            scanf("%lld",&D);


            E=(S-(A+B+C+D));
            printf("%lld\n",E);
            fflush(stdout);

            scanf("%lld",&Return);

                    if(Return==-1)
                        {
                        return 0;
                        }
                    if (Return==1)
                        {continue;}

   }
}
