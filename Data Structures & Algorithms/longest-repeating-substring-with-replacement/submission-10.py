class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        letter_freq = {}
        max_len = 0

        l = 0
        max_freq = 0
        for r in range(len(s)):
            letter_freq[s[r]] = letter_freq.get(s[r], 0) + 1
            max_freq = max(max_freq, letter_freq[s[r]])

            if (r - l +1) - max_freq > k:
                letter_freq[s[l]] -= 1              
                if letter_freq[s[l]] == 0:
                    letter_freq.pop(s[l])
                l+=1
            
            max_len = max(max_len, (r-l+1))
        
        return max_len
            