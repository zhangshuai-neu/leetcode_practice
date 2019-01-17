#include <stdio.h>

int binaryGap(int N) {
    int max_d = 0;  //max_distance
    const int AND_NUM=1;
    int count = 0;
    while(N!=0){
        count=0;
        //printf("%d\n",N);
        if(N&AND_NUM==1){
            count++;
            N=N>>1;
            // 按位与的优先级比较低
            while(N!=0 && (N&AND_NUM)==0){
                count++;
                N=N>>1;
            }
            if(N!=0 && N&AND_NUM==1){
                max_d = max_d>count? max_d:count;
                continue;
            }
            N=N>>1;
        } else {
            N=N>>1;
        }
    }
    return max_d;
}

int main(){
    printf("ret:%d\n",binaryGap(22));
    printf("ret:%d\n",binaryGap(5));
    printf("ret:%d\n",binaryGap(6));
}
