#include<stdio.h>
int main()
{
    int n=0;
    scanf("%d",&n);
    int min=0,max=0,count1=0,count2=0;
int arr[n];
for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    min=max=arr[0];
    for(int i=0;i<n;i++)
    {
        if(arr[i]>max)
        {
            max=arr[i];
            count1++;
        }

       else if(arr[i]<min)
        {
            min=arr[i];
            count2++;
        }

    }
    printf("%d %d",count1,count2);

}
