class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Classify before you code: the pattern, why it fits, the data structure, the target complexity, and your confidence from 1 to 5.

        #the pattern is going to be sliding window
        #the reason why is because the question asks for the length of the longest
        #substring, and a substring is a contiguous list of characters within a
        #string. therefore to accurately find the largest substring across the entire 
        #string, we'd need to use sliding window to move across the string
        #target complexity for time I'm thinking O(n), space, since we are detecting
        #duplicates, I believe our approach will use a set, which means an O(n) space
        #my confidence is a 4-5


        longest_len = 0
        win_set = set()
        l = 0
        for r in range(len(s)):

            while s[r] in win_set:
                win_set.remove(s[l])
                l+=1
            
            win_set.add(s[r])

            longest_len = max(longest_len, len(win_set))

        return longest_len


