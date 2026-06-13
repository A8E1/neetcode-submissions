class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram = words that can be re-arranged to == each other
            #must mean lengths are the same btwn strings
            #must mean letters used are the same btwn strings
            #must mean letter freq is the same btwn strings
        
        #simple check to take out cases where len != 
        if len(s) != len(t):
            return False
        
        #from now on, only dealing w/ cases where len is the same. 
        #does not mean letter freq || letters r ==

        lettersAndFreq = {}

        for i in range(len(s)):
            if s[i] in lettersAndFreq:
                lettersAndFreq[s[i]] += 1
            else:
                lettersAndFreq[s[i]] = 1

        for i in range(len(t)):
            if t[i] not in lettersAndFreq or lettersAndFreq[t[i]] == 0:
                return False
            else:
                lettersAndFreq[t[i]] -= 1

        return True
        



