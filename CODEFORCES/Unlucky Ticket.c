#include<stdio.h>
#include<string.h>
int main()
{
    int n=0;
    scanf("%d",&n);
    char str[2*n];
    scanf("%s",str);
    int a=n;
    for(int i=0;i<n;i++)
    {
        int b=a+1;
        for(int j=i+1;j<n;j++)
        {
            if(str[i]>str[j])
            {
                int temp=str[i];
                str[i]=str[j];
                str[j]=temp;
            }
              if(str[a]>str[b])
            {
                int temp1=str[a];
                str[a]=str[b];
                str[b]=temp1;
            }
            b++;
        }
        a++;
    }
    int count=0,count1=0;
    for(int i=0;i<n;i++)
    {
        int hold=n+i;
        if(str[i]>str[hold])
        {
            count++;
        }
        else if(str[i]<str[hold])
            {
            count1++;
            }
    }
    if(count==n||count1==n)
        printf("YES\n");

    else
    printf("NO\n");


}
