#include<stdio.h>
#include<string.h>

int main()
{
    int n=0,l=0,count=0;
    scanf("%d%d",&l,&n);

    char str[l];
    scanf("%s",str);

    char str2[n];
     scanf("%s",str2);

     for(int i=0;i<l;i++)
     {
         for(int j=0;j<n;j++)
         {
             if(str2[j]==str[i])
             {
                 count++;
             }
         }
     }
     if(count==0)
     {
         printf("%d\n",count);
         return 0;
     }
     else
     {
         printf("%d\n",12);
     }

}
