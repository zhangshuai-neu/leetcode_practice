# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """        
        nums_len = len(nums)
        if nums_len==0:
            return None
            
        max_index = 0
        max_num = nums[max_index]
        for i in range(nums_len):
            if nums[i] > max_num:
                max_num = nums[i]
                max_index  = i
        
        left = self.constructMaximumBinaryTree(nums[:max_index])
        right = self.constructMaximumBinaryTree(nums[max_index+1:])
        root = TreeNode(max_num)
        root.left = left
        root.right = right
        
        return root
        
