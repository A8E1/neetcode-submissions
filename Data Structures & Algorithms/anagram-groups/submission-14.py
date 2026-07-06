class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #a constructor used to build a dictionary whose values are preset as empty lists
        anagram_dict = defaultdict(list)

        for word in strs:
            #the key used to identify anagrams. anagrams will share this letter + freq breakdown.
            ascii_key = [0] * 26

            for letter in word:
                ascii_val = ord(letter) - ord('a')
                #will map the ascii value of the letter to 0->26

                ascii_key[ascii_val] += 1
            
            #dict keys cannot be mutable arrays, so we turn them into tuples
            ascii_key = tuple(ascii_key)

            #add the word to the list corresponding to it's letter_freq array code
            anagram_dict[ascii_key].append(word)


        
        return list(anagram_dict.values())

        