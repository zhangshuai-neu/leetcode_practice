class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # chr: ascii转字符
        #self.son_list = [chr(97+i) for i in range(26)]
        self.son_trie = [None for i in range(26)]
        # 是否末尾
        self.word_flag = False
    
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        word_len=len(word)
        # 97 == ord('a')
        index=ord(word[0])-97
        if self.son_trie[index]==None:
            self.son_trie[index]=Trie()
        
        if word_len>1:
            self.son_trie[index].insert(word[1:])
        else:
            self.son_trie[index].word_flag=True
              
                
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        result = False
        word_len=len(word)
        # 97 == ord('a')
        index=ord(word[0])-97
        if self.son_trie[index]!=None:
            if word_len>1:
                result = self.son_trie[index].search(word[1:])
            else:
                result= True and self.son_trie[index].word_flag
        return result
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        result = False
        word_len=len(prefix)
        # 97 == ord('a')
        index=ord(prefix[0])-97
        if self.son_trie[index]!=None:
            if word_len>1:
                result = self.son_trie[index].startsWith(prefix[1:])
            else:
                result= True
        return result
        
#------------------------------------
# 测试代码
#------------------------------------
t = Trie()
t.insert("cat")
t.insert("apple")



print(t.search('cat'))
#return True

print(t.startsWith('app'))
#return True

t.insert("app")
#return NULL

print(t.search('app'))
#return True

print(t.startsWith('c'))        
#return True

print(t.startsWith('d'))        
#return False

