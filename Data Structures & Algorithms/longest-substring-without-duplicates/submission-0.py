class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        maxWindowLength = 0

        for R in range(len(s)):

            while s[R] in window:
                maxWindowLength = max(maxWindowLength, len(window))
                window.remove(s[L])
                L += 1
                
            window.add(s[R])
        
        maxWindowLength = max(maxWindowLength, len(window))

        
        return maxWindowLength

