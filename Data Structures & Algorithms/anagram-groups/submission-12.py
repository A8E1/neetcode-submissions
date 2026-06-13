class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for word in strs:
            #each index of the key reps a letter
            ascii_key = [0] * 26

            for letter in word:
                ascii_val = ord(letter) - ord('a')
                ascii_key[ascii_val] += 1

            ascii_key = tuple(ascii_key)
            
            if ascii_key in anagram_dict:
                anagram_dict[ascii_key].append(word)
            else:
                anagram_dict[ascii_key] = [word]
            
        
        return list(anagram_dict.values())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # #decode each string into ascii key (array)
        # #strings with same ascii key = anagrams
        # ascii_dict = {}
        # for string in strs:
        #     ascii_key = [0] * 26
        #     for letter in string:
        #         ascii_val = ord(letter) - ord('a')
        #         ascii_key[ascii_val] += 1
        #     ascii_key = tuple(ascii_key)
        #     #keys cannot be mutable, must be immutable
        #     if ascii_key in ascii_dict:
        #         ascii_dict[ascii_key].append(string)
        #     else:
        #         ascii_dict[ascii_key] = [string]

        # return list(ascii_dict.values())
        
