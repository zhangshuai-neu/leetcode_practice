# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = head
        tail_count = 0
        while tail:
            tail = tail.next
            tail_count = tail_count + 1
        
        mid = head
        mid_count = tail_count//2-1
        
        while mid and mid_count>=0:
            mid = mid.next
            mid_count = mid_count-1
        return mid
