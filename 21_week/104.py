# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #===================
        # function
        #===================
        def get_next_level(cur_level_list):
            next_level_list = []
            for p_node in cur_level_list:
                if p_node.left != None:
                    next_level_list.append(p_node.left)
                if p_node.right != None:
                    next_level_list.append(p_node.right)
            return next_level_list
        
        #======================
        # 开始
        #======================
        if root==None:
            return 0
            
        cur_level_list = [root]
        deep_level = 1
        while True:
            cur_level_list = get_next_level(cur_level_list)
            if cur_level_list:
                deep_level = deep_level+1
            else:
                # list为空
                break
        return deep_level
                
