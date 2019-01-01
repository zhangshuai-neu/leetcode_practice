# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #采用前序遍历的做法
        def unival(root, uv):
            if root==None:
                return True
            return root.val==uv and unival(root.left, uv) and unival(root.right, uv)
            
        
        if root==None:
            return True
        return unival(root, root.val)
            
