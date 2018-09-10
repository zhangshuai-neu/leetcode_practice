class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 使用贪心法来解决
        # 每次走尽可能的远（局部最优）
        # 最后走的最远（全局最优）
        # notice：只要能够到达的位置(reach)比last_index大即可
        last_index = len(nums)-1
        reach = nums[0]
        i = 0
        while i<=reach and reach<last_index:
            reach = max(reach, i+nums[i])
            i=i+1

        print(reach>=last_index)    #debeg code
        
        return reach>=last_index

#-------------------------------------
# 测试代码
#-------------------------------------
s = Solution()

s.canJump([1,2,3])
# return Ture

s.canJump([3,2,1,0,4])
# return False

s.canJump([2,3,1,1,4])
# return True
