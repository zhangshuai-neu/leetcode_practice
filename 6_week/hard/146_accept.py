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
            node = self.lru_map[key]
            self.put(node.key,node.data)
            return node.data
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
            if self.head.key != node.key:
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
        head=self.head
        print("list_key:",end="")
        for i in range(self.len):
            print(head.key," ",end="")
            head=head.next
        print()

#==========================================
# 测试代码
#==========================================


""" test1
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
"""

func_list = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]

parameter_list = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

cache = LRUCache(10)
for i in range(len(func_list)):
    if func_list[i]=="put":
        print("put:",parameter_list[i][0],parameter_list[i][1])
        cache.put(parameter_list[i][0],parameter_list[i][1])
    else:
        print("get:",parameter_list[i][0])
        cache.get(parameter_list[i][0])
    
    cache.print_all()
    print()
    
    
    
    
    
