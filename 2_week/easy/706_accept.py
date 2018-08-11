class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #初始化hash_table，桶数为1000
        self.size = 1000
        self.hash_table = []
        for i in range(self.size):
            self.hash_table.append([])

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        bucket_index = key % self.size
        bucket_size = len(self.hash_table[bucket_index])
        i=0
        while i<bucket_size:
            #key是否存在
            if self.hash_table[bucket_index][i] == key:
                #存在，updata value
                self.hash_table[bucket_index][i+1] = value
                return
            i=i+2
        self.hash_table[bucket_index].append(key)
        self.hash_table[bucket_index].append(value)
        return 
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket_index = key % self.size
        bucket_size = len(self.hash_table[bucket_index])
        i=0
        while i<bucket_size:
            #key是否存在
            if self.hash_table[bucket_index][i] == key:
                #存在，返回value
                return  self.hash_table[bucket_index][i+1]
            i=i+2
        return -1
        
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        bucket_index = key % self.size
        bucket_size = len(self.hash_table[bucket_index])
        i=0
        while i<bucket_size:
            #key是否存在
            if self.hash_table[bucket_index][i] == key:
                #存在，删除
                self.hash_table[bucket_index].pop(i)
                self.hash_table[bucket_index].pop(i)
                return
            i=i+2
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


hashMap = MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            # returns 1
hashMap.get(3);            # returns -1 (not found)
hashMap.put(2, 1);         # update the existing value
hashMap.get(2);            # returns 1 
hashMap.remove(2);         # remove the mapping for 2
hashMap.get(2);            # returns -1 (not found) 
