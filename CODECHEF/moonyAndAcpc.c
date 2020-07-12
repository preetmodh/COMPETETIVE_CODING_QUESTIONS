#include<stdio.h>
int main()

{
    int T=0;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
        int n=0,max=0;
        scanf("%d",&n);

        int arr[n+4],arr1[n],arr2[4],arr3[4];
        for(int i=2;i<n+2;i++)
            scanf("%d",&arr[i]);

            if(n==3)
                max=arr[2]+arr[3]+arr[4];

            if(n==4)
            {
                arr3[0]=arr[2]+arr[3]+arr[4];
                arr3[1]=arr[2]+arr[3]+arr[5];
                arr3[2]=arr[2]+arr[4]+arr[5];
                arr3[3]=arr[3]+arr[4]+arr[5];
               for(int i=0;i<4;i++)
                {
                    if(arr3[i]>max)
                    max=arr3[i];
                }
            }

if(n>4)
{

           arr[0]=arr[n];
            arr[1]=arr[n+1];
            arr[n+2]=arr[2];
            arr[n+3]=arr[3];


        for(int i=2;i<n+2;i++)
        {
            arr2[0]=arr[i-2];
            arr2[1]=arr[i-1];
            arr2[2]=arr[i+1];
            arr2[3]=arr[i+2];

            int first=0,second=0;
            for(int j=0;j<4;j++)
            {
                if(arr2[j]>first)
                {
                    second=first;
                    first=arr2[j];
                }
                else if((arr2[j]>second)&&(arr2[j]<first))
                    second=arr2[j];
            }
            arr1[i-2]=first+second+arr[i];


        }
        for(int i=0;i<n;i++)
        {
            if(arr1[i]>max)
            max=arr1[i];
        }
}
        printf("%d\n",max);
    }
}
