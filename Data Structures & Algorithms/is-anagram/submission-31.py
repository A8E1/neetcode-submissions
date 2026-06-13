class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #properties of an anagram = 1. same len, 2. same letter freq. 3. same letters

        if len(s) != len(t):
            return False
        
        dict_of_s = {}
        dict_of_t = {}

        for char in s:
            if char in dict_of_s:
                dict_of_s[char] += 1
            else:
                dict_of_s[char] = 1

        for char in t:
            if char in dict_of_t:
                dict_of_t[char] += 1
            else:
                dict_of_t[char] = 1
        
        if dict_of_t != dict_of_s:
            return False
        else:
            return True

        
        # """
        #     # 2 steps to do: 1) check if length is same 2) check if same number of same key and values

        #     # check if length is same first as a first step
        #     if len(s) != len(t):
        #         return False 

        #     # Since length is same, now to check actual content of string
        #     # make 2 hash maps for each string
        #     countS, countT = {}, {}
            
        #     # parse through each in same for-loop and add one to each key, use .get(index, default value)
        #     for i in range(len(s)):
        #         countS[s[i]] = 1 + countS.get(s[i], 0)
        #         countT[t[i]] = 1 + countT.get(t[i], 0)
        #     # compare both dictionaries
        #     return countS == countT 
        # '''
