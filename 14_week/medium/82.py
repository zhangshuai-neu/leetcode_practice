# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def get(head):
            if head==None or head.next==None:
                return head
            hval = head.val
            cur = head.next
            flag = 0
            while cur!=None and cur.val==hval:
                cur=cur.next
                flag = 1
            if flag==1:
                return get(cur)
            head.next = get(cur)
            return head

        head = get(head)
        return head