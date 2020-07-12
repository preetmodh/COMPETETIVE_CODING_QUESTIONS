#include<stdio.h>
int main()
{
    int x1,v1,x2,v2;
    int count1=0,count2=0,ans1=0,ans2=0;

    scanf("%d%d%d%d",&x1,&v1,&x2,&v2);

    ans1=x1;
    ans2=x2;
    if(x2>=x1&&v2>v1)
        printf("NO");

    else
        {
                for(int i=0;i<10000;i++)
                {
                ans1=ans1+v1;
                count1++;
                ans2=ans2+v2;
                count2++;

                if((ans1==ans2)&&(count1==count2))
                            {
                                printf("YES");
                                break;
                            }

                }
                 printf("NO");
        }
}
