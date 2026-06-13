class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram characteristics:
            #equal len
            #same letters
            #same letter freq
        
        if len(s) != len(t):
            return False
        
        lettersAndFreq = {}
        #k/v = letter : freq

        for i in range(len(s)):
            if s[i] not in lettersAndFreq:
                lettersAndFreq[s[i]] = 1
            else:
                lettersAndFreq[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in lettersAndFreq or lettersAndFreq[t[i]] == 0:
                return False
            else:
                lettersAndFreq[t[i]] -= 1

        return True
