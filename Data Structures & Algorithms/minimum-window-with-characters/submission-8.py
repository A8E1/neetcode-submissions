class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}

        for letter in t:
            count_t[letter] = count_t.get(letter, 0) + 1
        
        formed = 0
        need = len(count_t)

        l = 0
        res, resLen = [-1,-1], float("infinity")

        win_count = {}
        for r in range(len(s)):
            c = s[r]
            win_count[c] = win_count.get(c, 0) + 1

            if c in count_t and count_t[c] == win_count[c]:
                formed += 1
            
            while formed == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l, r]
                win_count[s[l]] -= 1
                if s[l] in count_t and count_t[s[l]] > win_count[s[l]]:
                    formed -= 1

                l+=1
            
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""


        