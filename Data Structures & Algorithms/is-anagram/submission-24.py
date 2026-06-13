class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram characteristics:
            #equal len
            #same letters
            #same letter freq
        
        if len(s) != len(t):
            return False
        
        str1, str2 = {}, {}
        #k/v = letter : freq

        for i in range(len(s)):
            str1[s[i]] = 1 + str1.get(s[i], 0)
            str2[t[i]] = 1 + str2.get(t[i], 0)
            #safe hash map method to retrieve value but passes default val if none returned
        
        return str1 == str2
