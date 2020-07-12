#include<stdio.h>
#include<string.h>
int main()
{
        int t=0;
            scanf("%d\n",&t);
                for(int i=0;i<t;i++)
                    {
                        char str[10000];
                        gets(str);

                        for(int j=0;j<strlen(str);j=j+2)
                            printf("%c",str[j]);


                        printf(" ");

                        for(int k=1;k<strlen(str);k=k+2)
                            printf("%c",str[k]);


                        printf("\n");

    }
}
