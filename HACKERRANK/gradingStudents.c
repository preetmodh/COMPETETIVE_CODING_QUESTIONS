#include<stdio.h>
int main()
{
    int n=0,a=0;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);


        if(arr[i]<38)
            continue;

        else if(arr[i]%5==0)
            continue;

       else
       {
            a=arr[i]/5 +1;
            if((a*5-arr[i])<3)
                arr[i]=a*5;
       }
    }

              for(int i=0;i<n;i++)
                printf("%d\n",arr[i]);


}
