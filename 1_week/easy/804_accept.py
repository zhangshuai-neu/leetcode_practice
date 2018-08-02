class Solution:    
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def word_to_morse( word):
            morse_code_list =[ ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",	"..-","...-",".--","-..-","-.--","--.."]
            word_morse_code=""
            for i in range(len(word)):
                word_morse_code = word_morse_code + morse_code_list[ord(word[i]) - ord('a')]
            return word_morse_code;	
        
        morse_dict = {}
        for i in range(len(words)):
            morse_dict.setdefault(word_to_morse(words[i]), 1)
        return len(morse_dict)
