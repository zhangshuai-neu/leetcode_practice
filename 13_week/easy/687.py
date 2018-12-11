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
        记录 a-b 的长度
        记录 b-c 的长度
        记录 b-d 的长度
        
        """
        def path(root,val_dict):
            if root.val not in val_dict:
                val_dict.update({root.val:0})
                
            if root.left==None and root.right==None:
                return 0
            # 左侧
            left_val = 0
            if root.left!=None:
                if root.left.val == root.val:
                    left_val = path(root.left,val_dict)+1
                else:
                    path(root.left,val_dict)
                    
            # 右侧     
            right_val = 0
            if root.right!=None:
                if root.right.val == root.val:
                    right_val = path(root.right,val_dict)+1
                else:
                    path(root.right,val_dict)
            
            # 更新dict
            # 处理了多种情况，c-b-d形式
            # 1) right_val==0,left_val!=0
            # 2) right_val!=0,left_val==0
            # 3) right_val!=0,left_val!=0
            if root.val in val_dict  and val_dict[root.val]< right_val+left_val:
                val_dict[root.val] = right_val+left_val
            
            # 父亲节点需要这个数字 a-b-d 或者 a-b-c 形式
            return max(left_val,right_val)
        
        val_dict = {}
        if root!=None:
            path(root,val_dict)
            return max(val_dict.values())
        return 0
