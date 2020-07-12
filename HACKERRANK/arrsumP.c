                        //sum of array elements using pointers.
#include <stdio.h>
#include <stdlib.h>


int simpleArraySum(int array[],const int n)
{
    int sum=0,*ptr;
    int *const arrayEnd=array + n;
    for(ptr=array;ptr<arrayEnd;ptr++)
    {
        sum+=*ptr;
    }
        return sum;
}

int main()
{
    int m;
    scanf("%d",&m);
    int values[m];
    for(int i=0;i<m;i++)
    {
        scanf("%d",&values[i]);
    }
    printf("%d\n",simpleArraySum(values,m));
}
