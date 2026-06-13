class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #anagrams: words w/ same letters, same letter frequency, same length

        if len(s) != len(t):
            return False
        
        lettersAndFreq = {}
        #key: letter, value: freq

        for i in range(len(s)):
            if s[i] in lettersAndFreq:
                lettersAndFreq[s[i]] += 1
            else:
                lettersAndFreq[s[i]] = 1
            
        for i in range(len(t)):
            if t[i] in lettersAndFreq and lettersAndFreq[t[i]] != 0:
                lettersAndFreq[t[i]] -= 1
            else:
                return False
        return True