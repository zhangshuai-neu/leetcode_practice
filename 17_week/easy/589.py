"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def pre_order(root, ret_list):
            if root==None:
                return 
            ret_list.append(root.val)
            for node in root.children:
                pre_order(node, ret_list)
            return
        
        ret_list = []
        pre_order(root, ret_list)
        return ret_list
