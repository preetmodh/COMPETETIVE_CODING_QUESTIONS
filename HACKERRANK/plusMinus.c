#include<stdio.h>

int main()
{
        int n=0;
        float po=0,ne=0,ze=0;
        scanf("%d",&n);

        int arr[n];
        for(int i=0;i<n;i++)
            scanf("%d",&arr[i]);

           for(int i=0;i<n;i++)
           {
               if(arr[i]<0)
                   ne++;

                else  if(arr[i]>0)
                    po++;

                else
                    ze++;
           }

           ne=(float)ne/n;
           po=(float)po/n;
           ze=(float)ze/n;

           printf("%.6f\n",po);
           printf("%.6f\n",ne);
           printf("%.6f\n",ze);


}
