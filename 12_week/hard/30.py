class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # word可能重复，words可能为0
        # words长度
        words_len = len(words)
        if words_len == 0:
            return []
        
        # 获取word长度
        word_len = len(words[0])
        
        # 建立word词典
        word_dict = {}
        l=0
        for i in range(words_len):
            if words[i] not in word_dict:
                # value为[word_use_list的位置, word重复次数]
                word_dict.update({words[i]:[l,1]})
                l = l+1
            else:
                word_dict[words[i]][1] = word_dict[words[i]][1]+1
        word_dict_len = len(word_dict)
        
        # word使用情况记录, 每个word出现了几次
        word_use_list = [0 for i in range(word_dict_len)]
        
        # 结果list
        index_list = []
        start_index = 0
        start_flag = 0
        count = 0
        
        #遍历string
        i=0
        s_len = len(s)
        while i < s_len:
            word = s[i:i+word_len]
            if word in word_dict: 
                # 发现word  
                word_use_index = word_dict[word][0]
                
                # 第一次发现word
                if start_flag==0:
                    # 记录一下
                    start_flag = 1
                    start_index = i
                    # 清理word_use_list
                    for j in range(word_dict_len):
                        word_use_list[j] = 0
                
                # word过度重复,从start word的下一个字符开始
                if word_use_list[word_use_index] >= word_dict[word][1]:
                    # word过度重复,从start word的下一个字符开始
                    start_flag = 0
                    i = start_index+1
                    count = 0
                    continue
                    
                # 尚未出现过 或者 word尚未过度重复
                word_use_list[word_use_index] = word_use_list[word_use_index]+1
                count = count+1
                        
                # substring判断
                if count == words_len:
                    # 构成substring
                    index_list.append(start_index)
                    # 重新开始，从start word的下一个字符开始
                    start_flag = 0
                    i = start_index+1
                    count = 0
                    continue
                i=i+word_len
            else:
                # 不是word, 表示中间有间隔
                if start_flag==1:
                    # 重新开始，从start word的下一个字符开始
                    start_flag = 0
                    i = start_index+1
                    count = 0
                    continue
                i=i+1
       
        return index_list
        
# ok but 超时---------------------------
# 频繁的使用sum函数会超时，使用一个计数代替,大概差了0.07~0.1s 20%左右
"""
        # word可能重复，words可能为0
        # words长度
        words_len = len(words)
        if words_len == 0:
            return []
        
        # 获取word长度
        word_len = len(words[0])
        
        # 建立word词典
        word_dict = {}
        l=0
        for i in range(words_len):
            if words[i] not in word_dict:
                # value为[word_use_list的位置, word重复次数]
                word_dict.update({words[i]:[l,1]})
                l = l+1
            else:
                word_dict[words[i]][1] = word_dict[words[i]][1]+1
        word_dict_len = len(word_dict)
        
        # word使用情况记录, 每个word出现了几次
        word_use_list = [0 for i in range(word_dict_len)]
        
        # 结果list
        index_list = []
        start_index = 0
        start_flag = 0
        
        #遍历string
        i=0
        s_len = len(s)
        while i<s_len:
            word = s[i:i+word_len]
            if word in word_dict:
                word_use_index = word_dict[word][0]
                # 发现word  
                if start_flag==0:
                    # 如果是第一次发现word, 记录一下
                    start_flag = 1
                    start_index = i
                    # 清理word_use_list
                    for j in range(word_dict_len):
                        word_use_list[j] = 0
                    word_use_list[word_use_index]=1
                else:
                    # 不是第一个word
                    if word_use_list[word_use_index] >= word_dict[word][1]:
                        # word过度重复,从start word的下一个字符开始
                        start_flag = 0
                        i = start_index+1
                        continue
                    else:
                        # 尚未出现过 或者 word尚未过度重复
                        word_use_list[word_use_index] = word_use_list[word_use_index]+1
                        
                # substring判断
                if sum(word_use_list)==words_len:
                    # 构成substring
                    index_list.append(start_index)
                    # 重新开始，从start word的下一个字符开始
                    start_flag = 0
                    i = start_index+1
                    continue
                i=i+word_len
            else:
                # 不是word, 表示中间有间隔
                if start_flag==1:
                    # 重新开始，从start word的下一个字符开始
                    start_flag = 0
                    i = start_index+1
                    continue
                i=i+1
       
        return index_list
"""

#-----------

s = Solution()
"""
print(s.findSubstring("barfoothefoobarman",["foo","bar"]))

print(s.findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))

print(s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))

print(s.findSubstring("aaaaaaaa",["aa","aa","aa"]))

print(s.findSubstring("abaababbaba",["ab","ba","ab","ba"]))
"""
print(s.findSubstring("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab",["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba"]))





