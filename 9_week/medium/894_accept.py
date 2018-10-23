# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        global_result_list = []
        if N%2==0:
            #不可能
            return global_result_list

        if N==1:
            t=TreeNode(0)
            global_result_list.append(t)
            return global_result_list
        
        # N>=3
        # 逐步生成full binary tree，每次添加两个节点
        # n当前节点数，N最大节点数
        # 每次生成一个root，都要重新记录
        def add_node_in_fbt(root,)
        new_root=TreeNode(0)

        
            


