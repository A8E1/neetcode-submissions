class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}

        for letter in t:
            t_count[letter] = t_count.get(letter, 0) + 1
        
        have, need = 0, len(t_count)
        resLen = float("infinity")
        resInd = [-1, -1]

        win_count = {}

        l = 0
        for r in range(len(s)):
            win_count[s[r]] = win_count.get(s[r], 0) + 1

            if s[r] in t_count and win_count[s[r]] == t_count[s[r]]:
                have+=1
            
            while have == need:

                if r-l+1 < resLen:
                    resLen = r-l+1
                    resInd = [l, r]
                print(l)
                print(r)
                win_count[s[l]] -= 1

                if s[l] in t_count and win_count[s[l]] < t_count[s[l]]:
                    have-=1
                l+=1
            
        best_l, best_r = resInd
        return s[best_l:best_r+1] if resLen != float("infinity") else ""
