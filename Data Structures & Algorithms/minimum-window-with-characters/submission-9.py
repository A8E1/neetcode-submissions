class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #t can show up in any possible perm across the substring
        #since we're dealing wiht perms, it's similar to the anagram problem
        #i know for sure we'd need a letter frequency map for t, and a letter frequency map for the window we inspect
        #and the reasoning for sliding window here is pretty apparent, we're searching through a string for a substring
        #the key idea is how do we know we have a winning substring on our hands, which we take the length of?
        #we need to keep a tracker if each individual key in t_count has been found with the same freq within the substring
        #once we know that needed_keys == achieved_keys, we can take the length of that substring, and store it's corresponding indices
        #another aspect we need to take into account, is if a shorter substring exists within a valid substring
        #so once we clear a substring, within that while loop condition, we try to shorten the lengthb
        #the way we shorten, is by moving the left bound. with a condition:
        #checking if it led to a loss of an achieved_key. if it did, we break out the loop, and continue expanding right to find a 
        #new winning substring. 
        #we return the minimum substring that's corresponds to the indices + len we found

        min_len = float('infinity')
        res_index = [-1, -1]
        l = 0

        t_count = {}
        for letter in t:
            t_count[letter] = t_count.get(letter, 0) + 1
        
        achieved_keys = 0
        needed_keys = len(t_count)

        win_count = {}
        for r in range(len(s)):
            c = s[r]
            win_count[c] = win_count.get(c, 0) + 1

            if c in t_count and win_count[c] == t_count[c]:
                achieved_keys += 1
            
            while achieved_keys == needed_keys:
                if min_len > (r-l+1):
                    min_len = r-l+1
                    res_index = [l, r]

                #try to see if a shorter winning substring exists in the larger one we may be in
                left_char = s[l]
                if left_char in t_count and win_count[left_char] == t_count[left_char]:
                    achieved_keys -= 1
                win_count[left_char] -= 1
                
                l+=1
            
        l, r = res_index

        return s[l:r+1] if min_len != float('infinity') else ""