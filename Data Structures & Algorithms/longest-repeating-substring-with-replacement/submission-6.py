class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_freq = 0
        count = {}

        l = 0

        for r in range(len(s)):
            #build frequency map of all letters in the window
            count[s[r]] = count.get(s[r], 0) + 1

            #get the maximum frequency that exists within the window
            max_freq = max(max_freq, count[s[r]])

            #the invariant: where a window becomes invalid
            #when the # of replacements to make the window
            #a single character, exceeds k replacements
            while (r-l+1) - max_freq > k:
                count[s[l]] -= 1
                l+=1
            
            #once the window passes the invariant, we take
            #the length of the window, and replace if larger
            max_len = max(max_len, r-l+1)
        
        return max_len
            

            



        