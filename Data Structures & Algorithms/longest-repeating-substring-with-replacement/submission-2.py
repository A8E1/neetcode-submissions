class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #step 1: what is the output
            #we're looking for an integer that represents 
            #the LONGEST substring of the same character where we can replace up to k elements
        #step 2: what is the object we are searching
            #we're looking for a contiguous substring within a larger string
            #gives us da clue: sliding window!!
        #step 3: what's the invariant
            #the condition we're looking to keep true is that 
            #window_length - max frequency of the letters in the substring <= k
        #step 4: what's brute force:
            #count total frequencies in the each window
            #find max frequency in each window
            #if passes invariant, calculate length, replace if max
        #step 5: repeated work:
            #recounting previous frequencies
            #recalculating max frequency
        #step 6: state that could move work forward:
            #hashmap that only changes:
                # when new character added to window
                # when left side of window is moving inward
            #max frequency that only checks if newly added letter has > freq than previous max
        #step 7: form solution around new state

        l = 0
        max_len = 0
        letter_freq = {}
        max_freq = 0

        for r in range(len(s)):
            letter_freq[s[r]] = letter_freq.get(s[r], 0) + 1

            max_freq = max(max_freq, letter_freq[s[r]])

            while (r-l+1) - max_freq > k:
                letter_freq[s[l]] -= 1
                l+=1

            max_len = max(max_len, (r-l+1))

        return max_len 
            
        