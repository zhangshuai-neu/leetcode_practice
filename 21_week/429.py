"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root==None:
            return None
        
        # 记录节点信息
        deep_level = 0
        pre_deep_level = deep_level-1
        node_level_list = [[root]]
        
        # 记录节点的val信息 
        val_level_list = [[root.val]]
        
        while deep_level>pre_deep_level:
            pre_deep_level = deep_level
            next_level_flag = False
            
            node_cur_list = []  # 记录node
            val_cur_list = []   # 记录val
            for p_node in node_level_list[deep_level]:
                for node in p_node.children:
                    next_level_flag = True
                    node_cur_list.append(node)
                    val_cur_list.append(node.val)
            if next_level_flag:
                node_level_list.append(node_cur_list)
                val_level_list.append(val_cur_list)
                deep_level = deep_level +1

        print(val_level_list)
        return val_level_list
