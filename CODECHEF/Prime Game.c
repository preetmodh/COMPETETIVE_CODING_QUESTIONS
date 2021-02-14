#include <stdio.h>
#include <stdlib.h>
 
#define limit 1000000 /*size of integers array*/
long long int upper_bound(long long int arr[], long long int N, long long int X) 
{ 
    //printf("%lld %lld\n",N,X);
    //for (int I=0;I<N;I++){
      //  printf("%lld ",arr[I]);
    //}
    long long int mid=0; 
    long long int low = 0; 
    long long int high = N; 
  
    // Till low is less than high 
    while (low < high) { 
        // Find the middle index 
        mid = low + (high - low) / 2; 
  
        // If X is greater than or equal 
        // to arr[mid] then find 
        // in right subarray 
        if (X >= arr[mid]) { 
            low = mid + 1; 
        } 
  
        // If X is less than arr[mid] 
        // then find in left subarray 
        else { 
            high = mid; 
        } 
    } 
  
    // Return the upper_bound index 
    return low; 
} 


int main(){
    unsigned long long int i,j;
    int *primes;
 
    primes = malloc(sizeof(int) * limit);
    
    
    for (i = 2;i < limit; i++)
        primes[i] = 1;
 
    for (i = 2;i < limit; i++)
        if (primes[i])
            for (j = i;i * j < limit; j++)
                primes[i * j] = 0;
    int z=0;
    
    int cnt=0;
    for (i = 2;i < limit; i++)
        if (primes[i]){
            cnt+=1;
        }
        
    long long int a[cnt];
    for (i = 2;i < limit; i++)
        if (primes[i]){
            a[z]=i;
            z++;
        }
    
    
    
    int T=0;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
    int x,y;
    scanf("%d%d",&x,&y);
    if(y==1){
        if (x<=2){
            printf("Chef\n");
        }
        else{
            printf("Divyam\n");
        }
    }
    else{
        int cnt=0;
        long long int N = sizeof(a) / sizeof(a[0]);
        cnt=upper_bound(a,N, x);
        //printf("%d\n",cnt);
        if (y>=cnt){
            printf("Chef\n");
        }
        else{
            printf("Divyam\n");
        }
        }
    }
    
 
return 0;
}