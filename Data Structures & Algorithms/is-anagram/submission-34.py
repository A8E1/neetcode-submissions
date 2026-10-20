class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        for character in s:
            s_count[character] = s_count.get(character, 0) + 1
        for character in t:
            t_count[character] = t_count.get(character, 0) + 1
        
        if t_count == s_count:
            return True
        else:
            return False