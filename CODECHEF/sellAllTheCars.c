#include<stdio.h>
int main()
{
    int T=0;
    scanf("%d",&T);

    for(int t=0;t<T;t++)
    {
        int n=0;
        scanf("%d",&n);

        long long int arr[n];
        for(int i=0;i<n;i++)
            scanf("%lld",&arr[i]);


             for(int i=0; i<n; i++)
        {

            for(int j=i+1; j<n; j++)
            {

            if(arr[i] > arr[j])
                {
               long long int temp = arr[i];
                                    arr[i] = arr[j];
                                    arr[j] = temp;
                }
            }

    }



                long long int sum=0,j=0,a=0;
            for(int i=n-1;i>=0;i--)
        {

                a=(arr[i] - j);
                j++;
                if(a<=0)
                {
                    a=0;
                }
                sum=sum+a;
                sum=sum%1000000007;
        }

        printf("%lld\n",sum);

    }
}
