class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        anagram_dict = defaultdict(list)
        for word in strs:
            ascii_key = [0] * 26

            for letter in word:
                ascii_key[ord(letter) - ord('a')] += 1

            anagram_dict[tuple(ascii_key)].append(word)
        
        return list(anagram_dict.values())