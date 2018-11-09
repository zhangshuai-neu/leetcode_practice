class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 分成两侧，包含只出现一次的元素的一侧，元素数量为奇数。
        # 另一侧的元素数量为偶数。 single element一定在奇数侧

        # 利用二分法，不停寻找数量为奇数的一侧即可

        nums_len = len(nums)
        left = 0
        right = nums_len-1
        mid = (left+right)//2
        while True:
            flag = False
            if mid+1<nums_len and nums[mid]==nums[mid+1]:
                mid_left = mid
                mid_right = mid+1
                flag = True
            if mid-1>=0 and nums[mid]==nums[mid-1]:
                mid_left = mid-1
                mid_right = mid
                flag = True
            if flag == False:
                break

            left_len = mid_left-left
            right_len = right- mid_right

            if left_len%2==1:
                right = mid_left-1
            else:
                left = mid_right+1
            mid = (left+right)//2

        return nums[mid]


            
