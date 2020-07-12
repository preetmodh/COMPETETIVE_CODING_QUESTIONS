#include<stdio.h>

int main()
{
        int n=0;
        int count=0;

        scanf("%d\n",&n);

        int arr[n];
        for(int i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
        }
         for (int i = 0; i < n; ++i)
        {
            for (int j = i + 1; j < n; ++j)
            {
                if (arr[i] > arr[j])
                {
                    int temp =  arr[i];
                    arr[i]=arr[j];
                    arr[j] = temp;
                    count++;
                }
            }
        }

            printf("Array is sorted in %d swaps.\n",count);
            printf("First Element: %d\n",arr[0]);
            printf("Last Element: %d\n",arr[n-1]);

}
