#include <stdio.h>
#include <stdlib.h> //malloc，free
#include <limits.h> // INT_MAX,INT_MIN

int main() {
    int n;
    scanf("%d",&n);
    int i =0;
    int *a = (int*)malloc((n)*sizeof(int));
    long long max1,max2,max3,min1,min2;
    max1 = max2 = max3 = INT_MIN;
    min1 = min2 = INT_MAX;
    long long max; //确保是64bit
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
        // 处理max
        if( a[i]>max1 ){
            max3 = max2;
            max2 = max1;
            max1 = a[i];
        } else {
            if( a[i]>max2 ){
                max3 = max2;
                max2 = a[i];
            } else {
                if(a[i]>max3){
                    max3 = a[i];
                }
            }
        }
        // 处理min
        if( a[i]<min1 ){
            min2 = min1;
            min1 = a[i];
        } else {
            if( a[i]<min2 ){
                min2 = a[i];
            }
        }
    }
    printf("%d %d %d %d %d \n",max1,max2,max3,min2,min1);
    max = max1*max2*max3> max1*min1*min2? max1*max2*max3:max1*min1*min2;
    printf("%lld\n",max);
    return 0;
}
