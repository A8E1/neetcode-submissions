class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #output:
            #integer representing a length of longest substring
            #w/ k replacements
        #object being searched
            #substring
            #contiguous
            #sliding window 
        #invariant: substring window_size - max_freq <= k 
        #brute force: check every window

        max_freq = 0 
        max_len = 0
        count_map = {}
        l = 0

        for r in range(len(s)):
            count_map[s[r]] = count_map.get(s[r], 0) + 1
            max_freq = max(max_freq, count_map[s[r]])

            while (r - l + 1) - max_freq > k:
                count_map[s[l]] -=1
                l+=1
            
            max_len = max(max_len, r-l+1)
        
        return max_len




            