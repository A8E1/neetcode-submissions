class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #output
            #return an integer representing the max length of a substring 
            #that is one distinct character with at most k replacements to that substring
        #brute force
            #struggling to come up with brute force
        #observation
        #pattern
            #dynamic sliding window
        #invariant/state
            #valid when max_freq <= (len - k)
        #hash/window/decision step
            #keep letter frequency hashmap
        #complexity

        
        max_len = 0

        letter_freq = {}

        max_freq = 0
        l = 0
        for r in range(len(s)):

            letter_freq[s[r]] = letter_freq.get(s[r], 0) + 1

            max_freq = max(max_freq, letter_freq[s[r]])

            while (r - l + 1) - max_freq > k:
                letter_freq[s[l]] -= 1
                l+=1
            
            max_len = max(max_len, r - l + 1)

        return max_len
            
        




        