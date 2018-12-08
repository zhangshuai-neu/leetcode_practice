# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        """
            5(a)
            /
           5(b)
         /    \
        5(c)   5(d)
        
        经过某一节点的最长的path，可能有三种情况
        a-b-c
        a-b-d
        c-b-d
        需要计算三种情况的最大值，
        用deep记录 a-b 的长度
        用left记录 b-c 的长度
        用right记录 b-d 的长度
        """
        
        
