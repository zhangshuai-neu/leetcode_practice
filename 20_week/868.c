#include <stdio.h>

int binaryGap(int N) {
    int max_distance = 0;
    const int AND_NUM=1;
    int count = 0;
    while(N!=0){
        if(N&AND_NUM==1){
            sign=1;
            
        }
        if(N&AND_NUM==0){
            count = count+1
        }
        N=N>>1;
    }
    return max_distance;
}

int main(){
    int N = 9 ;
    int ret = binaryGap(N);
    printf("ret:%d\n",ret);
}
