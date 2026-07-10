class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}

        for letter in s1:
            s1_count[letter] = s1_count.get(letter, 0) + 1
        
        win_count = {}

        l = 0
        for r in range(len(s2)):

            win_count[s2[r]] = win_count.get(s2[r], 0) + 1

            if (r-l+1) == len(s1):
                if win_count == s1_count:
                    return True
                else:
                    win_count[s2[l]] -= 1
                    if win_count[s2[l]] == 0:
                        win_count.pop(s2[l])
                    l+=1
            
        return False
            

        