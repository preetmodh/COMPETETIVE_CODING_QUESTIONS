#include<stdio.h>
int main()
{
    int T=0;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
        int n=0;
        scanf("%d",&n);

        int arr[n];
        for(int i=0;i<n;i++)
            scanf("%d",&arr[i]);

        int count=10,ans=0,a=0;
          for(int i=0;i<n;i++)
          {
              if(arr[i]==1)
                {
                     a++;

                     if(count>=5)
                     ans=1;

                    else if(a!=1)
                        {
                            ans=0;
                            break;
                        }
                            count=0;
                }
              else if(arr[i]==0)
                {
                    count++;
                }
          }
            if(a==1)
                    printf("YES\n");

            else if(ans==1)
                printf("YES\n");

            else if(ans==0)
                 printf("NO\n");
        }
    }

