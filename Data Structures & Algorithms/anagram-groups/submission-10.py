class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #decode each string into ascii key (array)
        #strings with same ascii key = anagrams
        ascii_dict = {}
        for string in strs:
            ascii_key = [0] * 26
            for letter in string:
                ascii_val = ord(letter) - ord('a')
                ascii_key[ascii_val] += 1
            ascii_key = tuple(ascii_key)
            if ascii_key in ascii_dict:
                ascii_dict[ascii_key].append(string)
            else:
                ascii_dict[ascii_key] = [string]

        return list(ascii_dict.values())
        
