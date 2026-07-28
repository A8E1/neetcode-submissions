class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_count = {}
        mag_count = {}

        for letter in ransomNote:
            note_count[letter] = note_count.get(letter, 0) + 1
        
        for letter in magazine:
            mag_count[letter] = mag_count.get(letter, 0) + 1
        

        for letter in note_count.keys():
            if letter not in mag_count or note_count[letter] > mag_count[letter]:
                return False
        
        return True