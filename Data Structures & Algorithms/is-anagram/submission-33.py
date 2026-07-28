class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        for letter in s:
            s_count[letter] = s_count.get(letter, 0) + 1
        t_count = {}
        for letter in t:
            t_count[letter] = t_count.get(letter, 0) + 1
        
        return s_count == t_count