class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = defaultdict(list)
        #creates a dictionary (hashmap) whose default value is a List

        for string in strs:
            charCount = [0] * 26

            for char in string:
                charCount[ord(char) - ord("a")] += 1
                #ord gets the ascii value of the character
                #we need to map it to 0-26, so we subtract the initial letter ascii value "a"
            
            anagramList[tuple(charCount)].append(string)
            #can't hash lists since their mutable, so we use type cast into tuple 

        return list(anagramList.values())
            #we want to return a list value, not the default output from .values()
