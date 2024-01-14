from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        char_word1 = Counter(word1)
        char_word2 = Counter(word2)
        if char_word1 == char_word2:
            return True
        
        num_word1 = Counter(char_word1.values())
        num_word2 = Counter(char_word2.values())
        if num_word1 == num_word2 and set(word1) == set(word2):
            return True
        
        return False
