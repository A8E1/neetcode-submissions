class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for letter in s1:
            s1_freq[letter] = s1_freq.get(letter, 0) + 1
        
        win_freq = {}
        l = 0
        for r in range(len(s2)):
            win_freq[s2[r]] = win_freq.get(s2[r], 0) + 1

            if (r - l + 1) > len(s1):
                win_freq[s2[l]] -= 1
                if win_freq[s2[l]] == 0:
                    win_freq.pop(s2[l])
                l+=1
            
        
            if win_freq == s1_freq:
                return True
        
        return False