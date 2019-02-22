# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        def ArrayToNode(numList):
            numsLen = len(numList)
            if numsLen==0:
                return None
            mid = numsLen//2
            root =  TreeNode(numList[mid])
            root.left = ArrayToNode(numList[:mid])
            root.right = ArrayToNode(numList[mid+1:])
            return root
        return ArrayToNode(nums)
