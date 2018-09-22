class KthLargest:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.list_len=len(nums)
        self.list=nums.copy()
        self.list.sort()
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        big_index = self.list_len
        small_index = 0
        insert_index = (big_index+small_index)//2
        while small_index < big_index:
            if val > self.list[insert_index]:
                #注意+1
                small_index = insert_index+1
            else:
                big_index = insert_index
            insert_index = (big_index+small_index)//2
        
        self.list.insert(insert_index,val)
        self.list_len = self.list_len+1
        
        print(self.list[self.list_len-self.k])
        
        return self.list[self.list_len-self.k]
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#---------------------------
# 测试代码
#---------------------------
k=3
nums = [4,5,8,2];
kthLargest = KthLargest(k, nums);

kthLargest.add(3);   # returns 4
kthLargest.add(5);   # returns 5
kthLargest.add(10);  # returns 5
kthLargest.add(9);   # returns 8
kthLargest.add(4);   # returns 8
