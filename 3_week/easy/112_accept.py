# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def confirm_sum(root, acce_sum, sum):
            if root == None:
                return False
                
            ret_bool=False
            temp_sum = acce_sum + root.val
            if root.left==None and root.right==None:
                #末尾
                if temp_sum == sum:
                    ret_bool = ret_bool or True
            else:
                #非末尾
                if root.left!=None:
                    ret_bool = ret_bool or confirm_sum(root.left, acce_sum+root.val, sum)
                if root.right!=None:
                    ret_bool = ret_bool or confirm_sum(root.right, acce_sum+root.val, sum)
            return ret_bool
            
        return confirm_sum(root, 0, sum)
