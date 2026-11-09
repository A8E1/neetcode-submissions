class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_freq_s = {}
        letter_freq_t = {}

        for letter in s:
            letter_freq_s[letter] = letter_freq_s.get(letter, 0) + 1
        
        for letter in t:
            letter_freq_t[letter] = letter_freq_t.get(letter, 0) + 1

        
        return letter_freq_t == letter_freq_s