class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Classify before you code: the pattern, why it fits, the data structure, the target complexity, and your confidence from 1 to 5.

        #this is a sliding window problem. 
        #the reason why it fits is because the goal statement of this problem
        #is to find the length of the longest substring. substrings are contiguous
        #in nature, so to accurately evaluate substrings in an O(n) time, we need
        #we use a sliding window approach. 

        #the data structure i plan to use is a frequency hashmap
        #the reason being, I need to keep track of the largest frequency
        #of letters in the window.
        #that way I can check how many replacements I would need to make
        #to keep the window valid. 

        #time: O(n), where n represents length of input string. Space is
        #going to be O(1), since there are only 26 distinct possible keys
        #since the input is limited to upper case english characters, which there are
        #only 26 english characters. 

        
        #*pause*. Does that approach sound good?

        #confidence: 4-5


        maxLen = 0
        letter_freq = {}
        max_freq = 0
        l = 0
        for r in range(len(s)):
            letter_freq[s[r]] = letter_freq.get(s[r], 0) + 1
            max_freq = max(max_freq, letter_freq[s[r]])

            if (r - l + 1) - max_freq > k:
                letter_freq[s[l]] -= 1
                if letter_freq[s[l]] == 0:
                    letter_freq.pop(s[l])
                l+=1
            
            maxLen = max(maxLen, (r-l+1))
        
        return maxLen
                















