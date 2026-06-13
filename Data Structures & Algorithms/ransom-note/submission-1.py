class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_freq_magazine = {}

        for letter in magazine:
            letter_freq_magazine[letter] = letter_freq_magazine.get(letter, 0) + 1
        
        for letter in ransomNote:
            if letter not in letter_freq_magazine:
                return False
            
            letter_freq_magazine[letter] -= 1

            if letter_freq_magazine[letter] < 0:
                return False
        
        return True