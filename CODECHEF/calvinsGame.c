#include<stdio.h>
int max(int a,int b);
int main()
{
    int N, K,P=1,maxValue,count=0;
    scanf("%d %d",&N,&K);

    int Arr[N];
    int Arr1[2*N];
    int Arr2[2*N];

    for(int i=0;i<N;i++)
    {
        scanf("%d",&Arr[i]);
    }
    Arr[0]=Arr1[0];
    for(K;K<=N-1;K++)
    {
        if((Arr[K]<0)||(Arr[K+1]<0))
        {
        maxValue=max(Arr[K],Arr[K+1]);
        Arr1[P]=max;
        count=count + maxValue;
        P++;
                if(Arr[K+1]>Arr[K])
                {
                    K=K+1;
                }
        }
        else
        {
            Arr1[P]=Arr[K];
            count=count + Arr1[P];
            P++;
        }
    }
        printf("%d\n%d",count,K);
}





int max(int a,int b)
{
	if(a>b)
    	{
        	return a;
    	}
    	else
    	{
        	return b;
    	}
}
