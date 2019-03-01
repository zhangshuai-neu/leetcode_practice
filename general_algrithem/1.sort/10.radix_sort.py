class Solution:
    # 基数排序，对桶排序的改进版 
    # exp 表示要进行比较的位(个位，十位，百位等)
    def bucket_sort(self, num_list, exp):
        bucket_list = [ [] for i in range(10)]
        # 按照
        for val in num_list:
            bi = val //exp %10
            bucket_list[bi].append(val)
        # 恢复到num_list
        j = 0
        for i in range(10):
            for val in bucket_list[i]:
                num_list[j] = val
                j = j+1
    # 基数排序
    def radix_sort(self, num_list):
        max_num = max(num_list)
        exp = 1
        while max_num!=0:
            self.bucket_sort(num_list, exp)
            exp = exp*10
            max_num = max_num//10
        

#==================
s = Solution()
in_list = [81,93,11,700,23,54,69,3]
s.radix_sort(in_list)
print( in_list )

