class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        words_len = len(words)
        pattern_len = len(pattern)
        p2w_map = {}
        w2p_map = {}
        result_list = []
        for i in range(words_len):
            #判断一个word是否符合pattern
            flag = True
            word = words[i]
            word_len = len(word)
            p2w_map.clear()
            w2p_map.clear()
            #长度一致
            if word_len == pattern_len:
                for j in range(word_len):
                    wc=word[j]
                    pc=pattern[j]
                    if wc not in w2p_map and pc not in p2w_map:
                        w2p_map.update({wc:pc})
                        p2w_map.update({pc:wc})
                    else:
                        if pc in p2w_map and p2w_map[pc]!=wc:
                            flag=False
                            break
                        if wc in w2p_map and w2p_map[wc]!=pc:
                            flag=False
                            break
            if flag:
                result_list.append(words[i])
        return result_list
