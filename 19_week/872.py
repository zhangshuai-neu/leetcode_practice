# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaf(root, leaf_list):
            if root.left==None and root.right==None:
                leaf_list.append(root.val)
                return
            
            if root.left!=None:
                get_leaf(root.left, leaf_list)
                
            if root.right!=None:
                get_leaf(root.right, leaf_list)
            
        
        leaf_list1 = []
        leaf_list2 = []
        get_leaf(root1, leaf_list1)
        get_leaf(root2, leaf_list2)
        
        l1_len = len(leaf_list1)
        if l1_len!=len(leaf_list2):
            return False
        else:
            for i in range(l1_len):
                if leaf_list1[i]!=leaf_list2[i]:
                    return False
            return True
                
