# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def visit_root(row_level, root):
            val_level_result = []
            if root.left==None and root.right==None:
                val_level_result.append(root.val)
                val_level_result.append(row_level)
                return val_level_result
            #left和right同时存在
            if root.left!=None and root.right!=None:
                val_level_result_left=visit_root(row_level+1, root.left)
                val_level_result_right=visit_root(row_level+1, root.right)
                #比较level
                if val_level_result_left[1] < val_level_result_right[1]:
                    val_level_result = val_level_result_right
                else:
                    val_level_result = val_level_result_left
            else:
                #只有一侧
                if root.left!=None:
                    val_level_result=visit_root(row_level+1, root.left)
                else:
                    if root.right!=None:
                        val_level_result=visit_root(row_level+1, root.right)

            return val_level_result

        val_level_result = visit_root(0, root)
        return val_level_result[0]
