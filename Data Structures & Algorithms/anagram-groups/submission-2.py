class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listOfAnagrams = defaultdict(list)
        #need the values to be a list, so this is how we instantiate a dictionary of that nature

        for string in strs:
            letterFreq = [0] * 26
            #need an array of 26 to represent each letter. 
            #the numerical val at each index represents freq.
            #this is the array format we break each word down into. 
            #anagrams will have equivalent arrays

            for char in string:
                letterFreq[ord(char) - ord("a")] += 1

            listOfAnagrams[tuple(letterFreq)].append(string)
            #must type cast list into tuple bc lists aren't hashable
            #.append adds the string to the list val at the tuple key
            
        return list(listOfAnagrams.values())