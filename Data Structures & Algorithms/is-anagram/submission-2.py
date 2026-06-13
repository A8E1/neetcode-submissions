class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # 2 steps to do: 1) check if length is same 2) check if same number of same key and values

        # check if length is same first as a first step
        if len(s) != len(t):
            return False 

        # Since length is same, now to check actual content of string
        # make 2 hash maps for each string
        countS, countT = {}, {}
        
        # parse through each in same for-loop and add one to each key, use .get(index, default value)
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # compare both dictionaries
        return countS == countT 
