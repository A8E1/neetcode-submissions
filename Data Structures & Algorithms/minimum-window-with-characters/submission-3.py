class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count_t = {}

        for letter in t:
            count_t[letter] = count_t.get(letter, 0) + 1
        
        res = [-1, -1]
        res_len = float('infinity')

        formed = 0
        required = len(count_t) #num of keys

        win_count = {}
        l = 0
        for r in range(len(s)):
            win_count[s[r]] = win_count.get(s[r], 0) + 1

            if s[r] in count_t and win_count[s[r]] == count_t[s[r]]:
                formed += 1
            
            while formed == required:
                if (r-l + 1) < res_len:
                    res_len = r-l+1
                    res = [l, r]
                
                win_count[s[l]] -= 1
                if s[l] in count_t and win_count[s[l]] < count_t[s[l]]:
                    formed -= 1
                l+=1
            
        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""        