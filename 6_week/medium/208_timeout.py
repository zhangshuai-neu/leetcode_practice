class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #存放下一级Tire节点
        self.trie_son_list = []
        self.trie_son_len = 0
        #存放字符串
        self.char = '#'
        #是否为单词末尾
        self.flag = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        word_len = len(word)
        
        if self.trie_son_len==0:
            #创建新节点
            son_t = Trie()
            #将新节点存入父list中
            self.trie_son_list.append(son_t)
            self.trie_son_len=self.trie_son_len+1
            #word后续内容插入新节点
            son_t.char = word[0]
            if word_len>1:
                son_t.insert(word[1:])
            else:
                #单词结束标志
                son_t.flag=True
        
        for i in range(self.trie_son_len):  #遍历所有儿子节点
            if self.trie_son_len>0 and word[0]==self.trie_son_list[i].char:
                if word_len>1:
                    self.trie_son_list[i].insert(word[1:])
                else:
                    self.trie_son_list[i].flag=True
                break
            else:
                #创建新节点
                son_t = Trie()
                #将新节点存入父list中
                self.trie_son_list.append(son_t)
                self.trie_son_len=self.trie_son_len+1
                #word后续内容插入新节点
                son_t.char = word[0]
                if word_len>1:
                    son_t.insert(word[1:])
                else:
                    #单词结束标志
                    son_t.flag=True       

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        result = False
        word_len = len(word)
        for j in range(word_len):
            for i in range(self.trie_son_len):  #遍历所有儿子节点
                if self.trie_son_len>0 and word[0]==self.trie_son_list[i].char:
                    if word_len>1:
                        result = True and self.trie_son_list[i].search(word[1:])
                    else:
                        result = True and self.trie_son_list[i].flag
                    return result
        return result
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        result = False
        prefix_len = len(prefix)
        for j in range(prefix_len):
            for i in range(self.trie_son_len):  #遍历所有儿子节点
                if self.trie_son_len>0 and prefix[0]==self.trie_son_list[i].char:
                    if prefix_len>1:
                        result = True and self.trie_son_list[i].startsWith(prefix[1:])
                    else:
                        result = True
                    return result
        return result
        
#------------------------------------
# 测试代码
#------------------------------------
t = Trie()
t.insert("cat")
t.insert("apple")

print(t.search('cat'))
print(t.startsWith('app'))
t.insert("app")
print(t.search('app'))
print(t.startsWith('c'))
