class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val=None
        self.next=None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index<0:
            return -1
        
        temp=self
        while index>=0:
            if temp==None:
                return -1
            temp=temp.next
            index=index-1
        
        if temp==None:
            return -1
        
        return temp.val
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        new = MyLinkedList()
        new.val=val
        new.next=self.next
        self.next=new

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        new = MyLinkedList()
        new.val=val
        new.next=None
        
        temp=self
        while temp.next!=None:
            temp=temp.next
        temp.next=new
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index<0:
            return
        
        temp=self
        while index>=0:
            if temp==None:
                return
            pre=temp
            temp=temp.next
            index=index-1

        new=MyLinkedList()
        new.val=val
        pre.next=new
        new.next=temp
        
        
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index<0:
            return
        
        temp=self
        while index>=0:
            if temp==None:
                return
            pre=temp
            temp=temp.next
            index=index-1
        
        if temp!=None:
            pre.next=temp.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
