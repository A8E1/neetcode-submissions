class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #the size of the window depends the length of s1
        #we iterate thru s2 with that fixed window size, and we check if that window 
        #is a permutation of s1. the second we land on a perm, we return True
        #if we never return true, we return False at the end
        #the trick here is to find out how to verify if two sequences of letters are permutations
        #it may be similar to the anagram question. letters and freq must match
        #what we can do is create a set for every window we process that's pre-populated with the
        #letters in s1. and the logic revolves around operations with that set:
            #if the  letter in the window doesn't exist in the set, we move the left bound up
            #if the letter in the window does exist in the set, we remove that letter from the set, and 
            #process the next letter
        #if the set ends up empty after processing the window, we have return True
        
        s1_count = {}

        #build letter + freq map for s1
        for letter in s1:
            s1_count[letter] = s1_count.get(letter, 0) + 1
        
        l = 0
        window_count = {}
        for r in range(len(s2)):

            #build letter + freq map for window
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1

            #what makes a window invalid. when window size surpasses size of s1
            #we keep window_count state up to date, to match letter + freq within curr window
            while (r-l+1) > len(s1):
                window_count[s2[l]] -= 1
                #remove key the second we reach 0 for a letter
                if window_count[s2[l]] == 0:

                    window_count.pop(s2[l])
                l+=1
            
            if s1_count == window_count:
                return True
        
        return False
            
            
