#include<stdio.h>
int main()
{
    long long int arr[5],a=0;
    for(int i=0;i<5;i++)
    {
        scanf("%lld",&arr[i]);
    }
    for (int i = 0; i < 5; ++i)
        {
            for (int j = i + 1; j < 5; ++j)
            {
                if (arr[i] > arr[j])
                {
                    a =  arr[i];
                    arr[i] = arr[j];
                    arr[j] = a;
                }
            }
        }
        long long int max =arr[1]+arr[2]+arr[3]+arr[4];
        long long int min =arr[0]+arr[1]+arr[2]+arr[3];

        printf("%lld %lld",min,max);

}
