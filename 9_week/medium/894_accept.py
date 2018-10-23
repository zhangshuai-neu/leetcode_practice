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
        # root类表提交后，leetcode结果使用层序遍历表示
        # N只能是奇数
        # 先生成树，然后生成层序便利list
        # n记录是否生成完
        
        def get_all_FBT(N):
            tree_list=[]
            if N%2==0:
                return tree_list
            if N==1:
                tree_list.append(TreeNode(0))
                return tree_list

            n=N-1
            i=1
            while i<n:
                l_tree_list = get_all_FBT(i)
                r_tree_list = get_all_FBT(n-i)
                for k in range(len(l_tree_list)):
                    for j in range(len(r_tree_list)):
                        new_root = TreeNode(0)
                        new_root.left = l_tree_list[k]
                        new_root.right = r_tree_list[j]
                        tree_list.append(new_root)
                i=i+2
            return tree_list

        fbt_st_list=get_all_FBT(N)
        return fbt_st_list
