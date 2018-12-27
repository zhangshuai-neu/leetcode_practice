//这一题比较适合使用c语言
int getSum(int a, int b) {
    if(b==0)
        return a;
    
    int sum = a^b;
    int c = (a&b)<<1;
    return getSum(sum, c)
}