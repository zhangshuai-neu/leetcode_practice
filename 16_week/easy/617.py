# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def pre_order(t1, t2):
            if t1==None:
                return t2
            if t2==None:
                return t1
            t1.val = t1.val + t2.val
            
            t1.left = pre_order(t1.left, t2.left)
            
            t1.right = pre_order(t1.right, t2.right)
            
            return t1
        
        root = pre_order(t1, t2)
        return root
        
