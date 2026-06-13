class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroupings = defaultdict(list)

        for string in strs:
            lettersAndFreq = [0] * 26

            for char in string:
                lettersAndFreq[ord(char) - ord("a")] += 1
            
            anagramGroupings[tuple(lettersAndFreq)].append(string)

        return list(anagramGroupings.values())