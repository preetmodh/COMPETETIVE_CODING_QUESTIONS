#include<stdio.h>
int main()
{
    int n=0,count=0,ans=0;
    scanf("%d",&n);
    int arr1[n],arr2[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr1[i]);
        arr2[i]=0;
    }
    for(int i=0;i<n;i++)
    {
        count=1;
        for(int j=0;j<n;j++)
        {
            if(i==0&&arr1[i]==arr1[j])
            {
                count++;
            }
            else if(j<i &&arr1[i]==arr1[j])
                break;

             else if(j>i &&arr1[i]==arr1[j])
                    count++;
        }
        if(i==0)
            count--;

        arr2[i]=count/2;
        ans=ans+arr2[i];
    }
            printf("%d\n",ans);
}
