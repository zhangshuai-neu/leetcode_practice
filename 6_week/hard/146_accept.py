class LRUCache:
    class link_node:
        def __init__(self,key,data):
            self.key = key
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = None
        self.lru_map = {}
        self.len = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lru_map:
            self.put(key,self.lru_map[key].data)
            return self.lru_map[key].data
        else:
            return -1

        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.len==0:
            new_node = LRUCache.link_node(key,value)
            self.lru_map.update({key:new_node})
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.len = self.len+1
            return 

        if key in self.lru_map:
            node = self.lru_map[key]
            #提出
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            #插入原来的head之前
            head_prev_node = self.head.prev
            head_prev_node.next = node
            node.prev = head_prev_node
            node.next = self.head
            self.head.prev = node

            self.head = node
            node.data = value
        else:
            node = LRUCache.link_node(key,value)
            self.lru_map.update({key:node})
            #插入原来的head之前
            head_prev_node = self.head.prev
            head_prev_node.next = node
            node.prev = head_prev_node
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.len=self.len +1
            #过多
            if self.len>self.capacity:
                tail = self.head.prev
                tail_prev_node = tail.prev
                tail_prev_node.next = self.head
                self.head.prev = tail_prev_node
                self.lru_map.pop(tail.key)
                self.len=self.len-1

    def print_all(self):
        print(self.head.key)
        head=self.head.next
        while head!=self.head:
            print(head.key)
            head=head.next

#==========================================
# 测试代码
#==========================================



cache = LRUCache(2);

cache.put(1, 11)
cache.put(2, 12)

print(cache.get(1))
# returns 1

cache.put(3, 13)
# evicts key 2

print(cache.get(2))
# returns -1 (not found)

cache.put(4, 14)
# evicts key 1

print(cache.get(1))
# returns -1 (not found)

print(cache.get(3))
# returns 3

print(cache.get(4))             
# returns 4
