#include <stdio.h>

int main( )
{
    int a=0;
    int b=0;

    scanf("%d", &a);

    b=a%2;

    if(b==0&&(a>=6&&a<=20))
      printf("Weird");

    else if(b==0&&(a>20))
           printf("Not Weird");

    else if(b==0&&(a>=2&&a<5))
         printf("Not Weird");

    else if(b!=0)
        printf("Weird");


    return 0;
}


