#include<stdio.h>
int gcd(int a, int b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

// Function to find gcd of array of
// numbers
int findGCD(int *arr, int n)
{
    int result = arr[0];
    if(n!=1)
    {
        for (int i = 1; i < n; i++)
    {
        result = gcd(arr[i], result);

        if(result == 1)
        {
           return 1;
        }
    }
    }
    return result;
}

// Function to find lcm of array of
// numbers
int findLCM(int *arr, int n)
{
    // Initialize result
    int ans = arr[0];

    // ans contains LCM of arr[0], ..arr[i]
    // after i'th iteration,
   if(n!=1)
   {
       for (int i = 1; i < n; i++)
        ans = (((arr[i] * ans)) /
                (gcd(arr[i], ans)));
   }
    return ans;
}

int main()
{
    int n=0,m=0;
    scanf("%d%d",&n,&m);
    int arr1[n],arr2[m],count=0;

    for(int i=0;i<n;i++)
        {
            scanf("%d",&arr1[i]);
        }


        for(int i=0;i<m;i++)
            {
                scanf("%d",&arr2[i]);
            }

int x=findGCD(&arr2[0],m);
int y=findLCM(&arr1[0],n);



    for(int j=1;j<=x;j++)
    {
        int z=y*j;
        if(x%z==0)
            count++;
    }
                /*if(n==1||m==1)
                    count++;*/

        printf("%d\n",count);

}
