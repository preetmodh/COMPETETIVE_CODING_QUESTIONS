#include<stdio.h>
int main()
{
    char str[10];
    scanf("%s",str);

        if((str[8]=='A')&&((str[0]=='1')&&(str[1]=='2')))
        {
            str[0]='0';
           str[1]='0';
        }

    else if(str[8]=='P')
       {
           str[0]=str[0]+1;
           str[1]=str[1]+2;

       }


    for(int i=0;i<8;i++)
        printf("%c",str[i]);
}
