# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        origin_root = root
        new_node=TreeNode(val)
        
        if origin_root==None:
            origin_root = new_node
            return origin_root
        
        temp_root = origin_root
        while True:
            if val <temp_root.val:
                if temp_root.left==None:
                    temp_root.left = new_node
                    break
                else:
                    temp_root=temp_root.left
            else:
                if temp_root.right==None:
                    temp_root.right = new_node
                    break
                else:
                    temp_root=temp_root.right
        
        return origin_root
            
        
            
        
