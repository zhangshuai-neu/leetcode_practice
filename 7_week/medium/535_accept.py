class Codec:
    def __init__(self):
        self.l2s_map = {}
        self.s2l_map = {}
        self.hash_dict = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
    def encode(self, long_url):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        def hash_code():
            hash_str = ""
            for i in range(6):
                index = random.randint(0,61)
                hash_str = hash_str+self.hash_dict[index]    
            return hash_str
            
        short_url = "https://tinyurl.com/"+hash_code()
        while short_url in self.s2l_map:
            short_url = "https://tinyurl.com/"+hash_code()

        self.l2s_map.update({long_url:short_url})
        self.s2l_map.update({short_url:long_url})
        
        return short_url

    def decode(self, short_url):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return self.s2l_map.get(short_url)


#============================
# 测试代码
#============================
import random
c =  Codec()

s = c.encode("https://leetcode.com/problems/design-tinyurl")

s1 = c.decode(s)
