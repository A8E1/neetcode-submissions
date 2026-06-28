class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_freq = {}

        for letter in magazine:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

        for letter in ransomNote:
            if letter not in letter_freq:
                return False
            
            letter_freq[letter] -= 1

            if letter_freq[letter] < 0:
                return False
            
        
        return True
        