class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 使用贪心法来解决
        # 只能给出一条合理路径，不能给出最少 jump 次数的路径，唯一的反例[2,3,1]
        # 每次走尽可能的远（局部最优）
        # notice：只要能够到达的位置(reach)比last_index大即可

        print(nums)

        jump_count = 0
        last_index = len(nums)-1
        if last_index == 0:
            print(jump_count)
            return jump_count

        current_index = 0
        print("current_index:",current_index)
        while current_index<last_index:
            iter_next_index = current_index + 1
            max_reach = iter_next_index + nums[iter_next_index]
            while iter_next_index<=last_index and iter_next_index <= current_index + nums[current_index]:
                if max_reach<=iter_next_index + nums[iter_next_index]:
                    #必须要有等于，确保 max_current_index 会修改
                    max_current_index = iter_next_index
                    max_reach = max_current_index + nums[max_current_index]
                iter_next_index = iter_next_index+1
            current_index = max_current_index
            jump_count = jump_count+1
            print("current_index:",current_index)

            if current_index<last_index and max_reach>=last_index:
                current_index = last_index
                jump_count = jump_count+1
                print("current_index:",current_index)

        return jump_count
#-------------------------------------
# 测试代码
#-------------------------------------
s = Solution()

s.jump([1])
# return 0

s.jump([1,2])
# return 1

s.jump([1,2,3])
# return 2

s.jump([2,3,1,1,4,5])
# return 3
