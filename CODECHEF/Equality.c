#include<stdio.h>

int main()
{
    int N,Q;
    scanf("%d ",&N,&Q);
    int Query[N];
    for(int i=0;i<N;i++)
    {
        scanf("%d",&Query[i]);
    }
    for(int i=0;i<Q;i++)
    {
        int L,R;
        scanf("%d %d",&L,&R);

        int Query2[(R-L)+1];
        for (;L<=R;L++)
        {
         int index=0;
         Query2[index]=Query[L-1];
         index++

        }
    }

}
