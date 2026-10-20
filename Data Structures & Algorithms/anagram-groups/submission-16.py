class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped_anagrams = defaultdict(list)

        for string in strs:
            ascii_key = [0] * 26
            for letter in string:

                ascii_val = ord(letter) - ord('a')

                ascii_key[ascii_val] += 1
            
            ascii_key = tuple(ascii_key)
            grouped_anagrams[ascii_key].append(string)

        
        return list(grouped_anagrams.values())
                        

        