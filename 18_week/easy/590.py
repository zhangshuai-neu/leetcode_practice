"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def post_order(root, ret_list):
            if root==None:
                return 
            for node in root.children:
                post_order(node, ret_list)
            ret_list.append(root.val)
            return
            
        
        ret_list = []
        post_order(root, ret_list)
        return ret_list
