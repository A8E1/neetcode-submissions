class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        lettersAndFreq = [0] * 26
        for i in range(len(s)):
            lettersAndFreq[ord(s[i]) - ord("a")] += 1
            lettersAndFreq[ord(t[i]) - ord("a")] -= 1
        
        if [0] * 26 != lettersAndFreq:
            return False
        return True