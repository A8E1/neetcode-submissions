class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagrams = defaultdict(list)

        for string in strs:
            lettersAndFreq = [0] * 26
            for char in string:
                lettersAndFreq[ord(char) - ord("a")] += 1
            groupAnagrams[tuple(lettersAndFreq)].append(string)

        return list(groupAnagrams.values())