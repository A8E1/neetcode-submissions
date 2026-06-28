class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letter_freq = {}

        for letter in s:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1
        
        for letter in t:
            if letter not in letter_freq:
                return False
            
            letter_freq[letter] -= 1

            if letter_freq[letter] < 0:
                return False
        
        return True
        