class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #a data structure to store groups of anagrams
        #we need a way to identify the anagram

        #hashmap, key being the identifier for the anagram, value being the list of words

        anagramGroups = defaultdict(list)

        #anagram = letters that can be rearranged to equal another word
            #letters + letter freq == btwn anagrams

        for string in strs:
            letterFreq = [0] * 26
            #a -> z = 26 indicies

            for character in string:
                letterFreq[ord(character) - ord("a")] += 1
            
            anagramGroups[tuple(letterFreq)].append(string)
        
        return list(anagramGroups.values())

