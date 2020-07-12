#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int N=0,K=0;
        scanf("%d %d\n",&N,&K);

        char str[N];
        int count=N;
        int ans=0;



        for(int j=0;j<N;j++)
            {
                scanf("%c\n",&str[j]);
            }


            for(int z=0;z<K;z++)
            {
                if(str[count-1]=='T')
                    {
                        count--;
                    }

               else if(str[count-1]=='H')
                {
                for(int k=0;k<count;k++)
                {
                    if (str[k]=='T')
                       {
                           str[k]='H';
                       }
                    else  if (str[k]=='H')
                        {
                        str[k]='T';
                        }
                }
                        count--;
                }
            }
    for(int p=0;p<count+1;p++)
    {
        if(str[p]=='H')
            ans++;
    }
printf("%d",ans);

    }
}
