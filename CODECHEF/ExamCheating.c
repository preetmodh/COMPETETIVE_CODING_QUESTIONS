#include<stdio.h>
int main()
{
    int T;
    scanf("%d",&T);

    for(int i=0;i<T;i++)
    {
        long int A, B,set1,set2,p,ans=0;
        scanf("%ld%ld",&A,&B);

        for(p=1;;p++)
        {
            set1 = (A-1)%p;
            set2 = (B-1)%p;

            if((set1 == set2))
            {
               ans++;
            }
            if((A-1)&&(B-1)<p)
            {
               break;
            }
        }
            if(A==B)
                {
                ans=-1;
                printf("%ld",ans);
                }
           else printf("%ld",ans);

    }
}
