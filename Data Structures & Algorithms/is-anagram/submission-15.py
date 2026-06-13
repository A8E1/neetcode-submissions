class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #letters r the same. 
        #order is different.
            #this means simple letter by letter check is not possible
            #ex: single loop that checks curr index of s and t
            #means length of both strings MUST be the same

        
        
        #brute force solution: nested for loop that exits when letter not present in a string is found

        #possible solution

        #since I know that best case space/time is O(1) and O(n+m), that gives me two hints:
            #1. no new data structures need to be made
            #2. n + m means two forloops SEQUENTIALLY. Not nested

        #lets think abt this. what can I do with two for loops sequentially? w/o creating new data structures?

        #only sol that's coming to MY mind is: iterating once, creating list of letters

        #iterate thru second word, EXIT if letter not in list, each check, remove that letter from list.


        letters_word1 = {}

        #takes out cases w/ same letters but not same length (not != freq of letters tho)
        if len(s) != len(t):
            return False


        #strictly dealing w/ same length, now have to figure out if same letters

        #anagrams MUST have same # of each letter as well. That's why not only same letters, 
        #but same freq of letters must be tracked

        # lettersAndFreq = {}
        # for i in range(len(s)):
        #     if s[i] in lettersAndFreq:
        #         lettersAndFreq[s[i]] += 1
        #     else:
        #         lettersAndFreq[s[i]] = 1 
        
        # for i in range(len(t)):
        #     if t[i] in lettersAndFreq and lettersAndFreq[t[i]] != 0:
        #         lettersAndFreq[t[i]] -= 1
        #     else:
        #         return False

        lettersT, lettersS = {}, {}

        for i in range(len(s)):
            lettersS[s[i]] = 1 + lettersS.get(s[i], 0)
            lettersT[t[i]] = 1 + lettersT.get(t[i], 0)

        for letter in lettersT:
            if lettersT[letter] != lettersS.get(letter):
                return False

        return True
            

                


