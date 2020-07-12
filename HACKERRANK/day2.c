#include<stdio.h>
#include<math.h>
int main()
{
    double meal=0;
    int tip=0;
    int tax=0;

    scanf("%lf",&meal);
    scanf("%d",&tip);
    scanf("%d",&tax);

    double ans=meal + (meal*tip/100) + (meal*tax/100);




    printf("%.0lf",round(ans));
}
