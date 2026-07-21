class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        shared_letters = {}
        res = []

        for letter in words[0]:
            shared_letters[letter] = shared_letters.get(letter, 0) + 1
        
        for i in range(1, len(words)):
            word_count = {}

            for letter in words[i]:
                word_count[letter] = word_count.get(letter, 0) + 1

            for letter in shared_letters:
                if letter not in word_count:
                    shared_letters[letter] = 0
                
                elif word_count[letter] < shared_letters[letter]:
                    while word_count[letter] < shared_letters[letter]:
                        shared_letters[letter] -= 1
                
                else:
                    continue
        
        for letter in shared_letters.keys():
            for i in range(shared_letters[letter]):
                res.append(letter)
        
        return res
            
