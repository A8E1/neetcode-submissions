class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}

        max_len = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            #build count_map for this window
            #key with largest count is the primary letter in the window
            #while window_length - primary_letter_count > k, move l up.
                #why: as long as window_length - primary_letter_count <= k, 
                #it means that we can make k replacements and get a 
                #contiguous substring w/ one distinct char
                #the second that condition is violated we need to move l up by 1. 
                #we re-calculate the count_map, and check the if again.
            #else: calc substring len, replace max_len if needed, continue to move r forward. 

            #count_map built
            count_map[s[r]] = count_map.get(s[r], 0) + 1
            max_freq = max(max_freq, count_map[s[r]])

            #moving left bound up until condition is satisfied
            while (r-l+1) - max_freq > k:
                count_map[s[l]] -= 1
                l+=1
            

            
            #replacing max_len if it's the longest valid window 
            max_len = max(max_len, r - l+1)
        
        return max_len
