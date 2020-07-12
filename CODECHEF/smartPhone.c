#include <stdio.h>
int main()
{
    long long int max=0,fix;
    int N;
    scanf("%d",&N);
    long long int budget[N];
    long long int p[N];

    for(int i=0;i<N;i++)
        {
               scanf("%lld",&budget[i]);
        }
        for(int i=0;i<N;i++)
        {

            fix=budget[i];
            long long int revenue=0;

            for(int j=0;j<N;j++)
            {
                if(budget[j]>=fix)
                {
                    revenue=revenue+fix;
                }

            }
                p[i]=revenue;

                if(max<p[i])
                {
                    max=p[i];
                }

        }
        printf("%lld",max);
}
