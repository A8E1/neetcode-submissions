class Solution:


#have the length of the string first, then a delimiter, and then the word
    def encode(self, strs: List[str]) -> str:

        res = ""
        for word in strs:
            length = len(word)
            res += str(length) + "#" + word
        
        return res




    def decode(self, s: str) -> List[str]:
        res = []

        i, j = 0, 0

        while i < len(s):
            
            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])

            i = j+1

            j = i + length

            word = res.append(s[i:j])
            
            i = j
        
        return res









