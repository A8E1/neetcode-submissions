class Solution:

    def encode(self, strs: List[str]) -> str:
        #first, we put all lengths in the beginning of the string
        #next a delimiter 
        #then each word in the same order of the lens

        if not strs:
            return ""

        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
       
        return res
        
        

    def decode(self, s: str) -> List[str]:
       #we need a list tracking each size we grab from the string
       #then using that list grab a list of strings
       
        if s == "":
            return []
        
        i, j, strings = 0, 0, []

        while i < len(s):

            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            strings.append(s[i:j])
            i = j


        
        return strings
        
