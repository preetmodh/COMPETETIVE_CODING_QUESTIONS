#include<stdio.h>
#include<string.h>
int main()
{
    int n=0,m=0,count=0;
    scanf("%d%d",&n,&m);
    int size=m+n;

    char strings[size][1000];
    for(int i=0;i<n+m;i++)
    {
        scanf("%s",strings[i]);
    }

    if(n>m)
    {
        printf("YES\n");
        return 0;
    }
    else if(n<m)
    {
            printf("NO\n");
            return 0;
    }

    else
        {
            for(int i=0;i<n;i++)
            {
                for(int j=n;j<m+n;j++)
                {
                    if(strcmp(strings[i],strings[j])==0)
                    {
                        count++;
                        break;
                    }
                }
            }
            if(count>0&&count<n)
                printf("YES\n");
            else if((count==n)&&(count%2==0))
                printf("NO\n");
            else if((count==n)&&(count%2!=0))
             printf("YES\n");
            else
            printf("NO\n");

        }
}
