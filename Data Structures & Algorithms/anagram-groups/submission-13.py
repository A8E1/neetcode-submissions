class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for word in strs:
            ascii_key = [0] * 26

            for letter in word:
                ascii_val = ord(letter) - ord('a')
                ascii_key[ascii_val] += 1
                
            ascii_key = tuple(ascii_key)
            
            anagram_dict[ascii_key].append(word)
        
        return list(anagram_dict.values())



