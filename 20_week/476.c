int findComplement(int num) {
        //记录2的k次方
        int two_k = 1;
        while(two_k<num){
            two_k = (two_k<<1) +1;
        }
        return num^two_k;
}
