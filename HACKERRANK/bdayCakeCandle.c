#include<stdio.h>
int main()
{
    int n=0,max=0,count=0;
        scanf("%d",&n);

        int arr[n];
        for(int i=0;i<n;i++)
            scanf("%d",&arr[i]);

        for(int i=0;i<n;i++)
        {
            if  (arr[i]>max)
                max=arr[i];
        }
         for(int i=0;i<n;i++)
         {
             if(arr[i]==max)
                count++;
         }

            printf("%d\n",count);


}
