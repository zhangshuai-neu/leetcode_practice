#=====================
# search tree 节点类
#=====================
class SearchTreeNode:
    val = 0
    key = 0 # 可以是任何类型, 不可修改
    left = None
    right = None
    # 统计左右子树的节点数量
    left_num = 0
    right_num = 0
    
    def __init__(self, key ,val):
        self.val = val
        self.key = 0
        self.left = None
        self.right = None
        self.left_num = 0
        self.right_num = 0
    
    def get_key(self):
        return self.key
    
    def get_val(self):
        return self.val
        
    def set_val(self, val):
        self.val = val
    
    def get_left(self):
        return self.left
    
    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right
    
    def set_right(self, node):
        self.right = node
    
    def add_left_num(self):
        self.left_num = self.left_num+1
    
    def dec_left_num(self):
        if self.left_num>0:
            self.left_num = self.left_num-1
    
    def add_right_num(self):
        self.right_num = self.right_num+1
    
    def dec_right_num(self):
        if self.right_num>0:
            self.right_num = self.right_num-1
        
#=====================
# 二叉搜索树
#=====================
class SearchTree:
    root = None
    
    # 插入查找树节点
    def insert(self, st_node):
        if self.root = None:
            self.root = st_node
        else:
            key = st_node.get_key()
            temp_node = self.root
            pre_temp_node = self.root
            is_left = False
            while temp_node!=None:
                if key<temp_node.get_key():
                    pre_temp_node = temp_node
                    temp_node = temp_node.get_left()
                    
                    is_left = True
                else:
                    pre_temp_node = temp_node
                    temp_node = temp_node.get_right()
                    is_left = False
            if is_left:
                pre_temp_node.set_left(st_node)
                pre_temp_node.add_left_num()
            else:
                pre_temp_node.set_right(st_node)
                pre_temp_node.add_right_num()
    
    # 获得当前节点的后继节点
    def get_min(self, root):
        temp_node = root
        while temp_node.get_left() != None:
            temp_node = temp_node.get_left()
        return temp_node
    
    # 删除key对应的节点
    def remove(self, key):
       temp_node = self.root
       pre_temp_node = self.root
       is_left = False
       while temp_node!=None:
            if key<temp_node.get_key():
                pre_temp_node = temp_node
                temp_node = temp_node.get_left()
                is_left = True
            else:
                if key>temp_node.get_key():
                    pre_temp_node = temp_node
                    temp_node = temp_node.get_left()
                    is_left = False
                else:
                    break
        
        if temp_node == None:
            return None
            
        if is_left:
            min_right = self.get_min(temp_node.get_right())
            if min_right==None:
                pre_temp_node.set_left(temp_node.get_left())
            else:
                
        else:
            
        
    
    # 返回key对应的value
    def get(slef, key):
        temp_node = root
        while temp_node!=None:
            if key == temp_node.get_key():
                return temp_node.get_val()
                
            if key<temp_node.get_key():
                temp_node = temp_node.get_left()
            else:
                temp_node = temp_node.get_right()
        return None
