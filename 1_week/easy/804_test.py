def word_to_morse(word):
	morse_code_list =[ ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",	"..-","...-",".--","-..-","-.--","--.."]
	word_morse_code=""
	for i in range(len(word)):
		word_morse_code = word_morse_code + morse_code_list[ord(word[i]) - ord('a')]
	return word_morse_code;	
	
words = ["gin", "zen", "gig", "msg"]
morse_dict = {}
for i in range(len(words)):
	morse_dict.setdefault(word_to_morse(words[i]), 1)

print(len(morse_dict))


