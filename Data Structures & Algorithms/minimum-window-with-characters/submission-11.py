class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}

        for letter in t:
            t_count[letter] = t_count.get(letter, 0) + 1
        
        need = len(t_count)
        have = 0

        res_len = float('infinity')
        res_indices = [-1, -1]

        l = 0

        win_count = {}

        for r in range(len(s)):
            win_count[s[r]] = win_count.get(s[r], 0) + 1

            if s[r] in t_count and win_count[s[r]] == t_count[s[r]]:
                have += 1
            
            while need == have:
                if (r-l+1) < res_len:
                    res_len = r-l+1
                    res_indices = [l, r]

                win_count[s[l]] -= 1

                if s[l] in t_count and win_count[s[l]] < t_count[s[l]]:
                    have-=1

                l+=1
        
        l, r = res_indices
        return s[l : r + 1] if res_len != float('infinity') else ""
