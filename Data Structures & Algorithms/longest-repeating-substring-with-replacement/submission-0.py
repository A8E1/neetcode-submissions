class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        
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
            count_map = {}

            for i in range(l, r+1):
                count_map[s[i]] = count_map.get(s[i], 0) + 1

            #finding letter that has highest freq in window
            primary_letter = s[l]
            for letter, freq in count_map.items():
                if freq > count_map[primary_letter]:
                    primary_letter = letter
            
            #moving left bound up until condition is satisfied
            while (r-l+1) - count_map[primary_letter] > k:
                l+=1
            
            #replacing max_len if it's the longest valid window 
            max_len = max(max_len, r - l+1)
        
        return max_len
