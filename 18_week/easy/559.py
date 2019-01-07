"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def get_deep(root):
            if root==None:
                return 0
            else:
                max_deep = 0
                for node in root.children:
                    max_deep = max( max_deep, get_deep(node) )
                max_deep = max_deep+1
                return max_deep
            
        return get_deep(root)
