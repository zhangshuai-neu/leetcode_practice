class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        
        #{key,[value,[prev],[next]]}
        #借用list生成前后索引，建立fifo循环链表
        #[value,[prev],[next]]作为节点
        self.lru_map  = {}
        self.lru_head = [None,[0],[0]]
        self.lru_len  = 0
        self.value=0
        self.prev=1
        self.next=2

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.lru_map:
            
        else:
            return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.lru_len==0:
            #插入
            self.lru_map.update({key,[value,[0],[0]]})
            #维护lru
            self.lru_head[self.prev] = lru_map[key]
            self.lru_head[self.next] = lru_map[key]
            self.lru_len = self.lru_len+1
            return
        
        if key in self.lru_map:
            self.lru_map[key][self.value]=value
            self.lru_map[key][self.prev]=self.lru_head
            self.lru_map[key][self.next]=self.lru_head[self.next]
        else:
            
            


#==========================================
# 测试代码
#==========================================



cache = LRUCache( 2);

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       # returns 1
cache.put(3, 3);    # evicts key 2
cache.get(2);       # returns -1 (not found)
cache.put(4, 4);    # evicts key 1
cache.get(1);       # returns -1 (not found)
cache.get(3);       # returns 3
cache.get(4);       # returns 4
