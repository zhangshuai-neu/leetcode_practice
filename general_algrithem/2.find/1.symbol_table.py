class MySymbolTable:
    key_value_list = []
    count = 0
    # key是string类型，Value是int
    def put(self, key, value):
        if self.contains(key):
            print("Key is in SymbolTable")
        else:
            self.key_value_list.append([key, value])
            self.count = self.count+1
        
    def get(self, key):
        if self.contains(key):
            index = self.contains(key) -1
            return self.key_value_list[index][1]
        else:
            print("Key is NOT in SymbolTable")
            return None
    
    def delete(self, key):
        if self.contains(key):
            index = self.contains(key) - 1
            self.key_value_list.pop(index)
            self.count = self.count-1
        else:
            print("Key is NOT in SymbolTable")
    
    # 返回第几个元素(不是索引号)，0表示key不ST中
    def contains(self, key):
        for i in range(self.count):
            if key== self.key_value_list[i][0]:
                return i+1
        return 0
    
    def size(self):
        return self.count
    
    def is_empty(self):
        return self.count==0
        
#================
# 测试
#================
my_st = MySymbolTable()
my_st.put("A",1)
my_st.put("B",2)
my_st.put("D",4)
my_st.put("C",3)

print( "my_st.is_empty():", my_st.is_empty() )
print( "my_st.size():", my_st.size() )
print( "my_st.get():", my_st.get("A") )
print( "my_st.get():", my_st.get("B") )
print( "my_st.get():", my_st.get("C") )
print( "my_st.get():", my_st.get("D") )
print( "my_st.delete():", my_st.delete("B") )
print( "my_st.delete():", my_st.delete("C") )
print( "my_st.size():", my_st.size() )








