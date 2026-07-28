class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            length = len(string)

            res += str(length) + "#" + string

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        l = 0
        while l < len(s):

            length = ""
            while s[l].isnumeric():
                length += s[l]
                l+=1
            
            if length:
                length = int(length)
                l+=1
                extracted_string = s[l:l+length]
                res.append(extracted_string)
                l += length

            
        return res
            