class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxLen = 0
        maxFreq = 0

        win_count = {}
        for r in range(len(s)):
            win_count[s[r]] = win_count.get(s[r], 0) + 1

            maxFreq = max(maxFreq, win_count[s[r]])

            if (r-l+1)-maxFreq > k:
                win_count[s[l]] -= 1
                l+=1

            maxLen = max(maxLen, r-l+1)
        
        return maxLen