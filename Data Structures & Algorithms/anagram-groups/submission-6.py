class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #need a way to breakdown each word
        #find a way to make anagrams identifiable
        #anagrams have === letters + freq.

        anagramGroup = defaultdict(list)

        for string in strs:
            letterFreq = [0] * 26
            for char in string:
                letterFreq[ord(char) - ord("a")] += 1
            anagramGroup[tuple(letterFreq)].append(string)

        return list(anagramGroup.values())
      