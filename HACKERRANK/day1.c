#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
 {
    int i = 4;
    double d = 4.0;
    char s[] = "HackerRank ";

    int I = 0;
    double D = 0.0;
    char str[1000];

    scanf("%d",&I);
    scanf("%lf\n",&D);


    gets(str);



    printf("%d\n",i+I);
    printf("%.1lf\n",d+D);
    printf("%s",strncat(s,str,strlen(input)));



    return 0;
}
