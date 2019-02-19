# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #===================
        # function 获取
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
            return []
        
        cur_level_list = [root]
        val_level_list = [[root.val]]
        while True:
            cur_level_list = get_next_level(cur_level_list)
            val_cur_level_list = []
            if cur_level_list:
                for node in cur_level_list:
                    val_cur_level_list.append(node.val)
                val_level_list.append(val_cur_level_list)
            else:
                # list为空
                break
        val_level_list.reverse()
        return val_level_list
