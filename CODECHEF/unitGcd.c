#include<stdio.h>
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int main()
{
    int T=0;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
        int n=200,a=0,count=0;
        int arr[n],arrP[n];



        for(int i=0;i<n;i++)
        {
            arrP[i]=0;
            arr[i]=i+1;
            if(arr[i]==9||arr[i]==25||arr[i]==49)
            {
                arr[i]=0;
            }
        }
    scanf("%d",&n);
    printf("%d\n",n/2);

    for(int i=0;i<n;i++)
     {
           int isPrime=0;
           for(int j=2;j<i;j++)
           {
                 if(arr[i]%j==0)
                 {
                       isPrime=1;
                       break;
                 }
           }
           if(isPrime==0)
           {
                arrP[a]=arr[i];
                count++;
                arr[i]=0;
                a++;
           }
     }
     printf("%d ",count);
     for(int i=0;i<n;i++)
     {
         if(arrP[i]!=0)
         printf("%d ",arrP[i]);
     }
     printf("\n");
     count=0;

     int psquare[3]={9,25,49};
     for(int i=0;i<3;i++)
     {
         if(psquare[i]<=n)
            {
                count++;
            }
            else
            {
                psquare[i]=0;
            }
     }
     if(n>=9)
        arr[3]=0;
        if(n>=9)
printf("%d ",count+1);
  for(int i=0;i<3;i++)
  {
      if(psquare[i]!=0&&n>=4)
         {
             if(i==0)
                printf("4 ");

                printf("%d ",psquare[i]);
         }
  }
  if(n>=9)
    printf("\n");
  count=0;
  for(int i=0;i<n;i++)
  {
      if(arr[i]%2!=0)
        count++;
  }
  for(int i=0;i<n;i++)
  {

      if(arr[i]%2==0&&arr[i]!=0)
      {
          if(count>0)
          {
              printf("2 ");
              printf("%d ",arr[i]);
              count--;
              arr[i]=0;
          }
          else if(count<=0)
          {
               printf("1 ");
              printf("%d ",arr[i]);
              arr[i]=0;
              printf("\n");
          }
      }
      else if(arr[i]%2!=0&&arr[i]!=0)
      {
          printf("%d ",arr[i]);
          arr[i]=0;
      }
  }
  printf("\n");

    }
}




