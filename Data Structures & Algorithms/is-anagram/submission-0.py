class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # checks if same length
        if len(s) != len(t):
            return False

        # after making new list sorting each string, it checks if they are the same ASCII value
        return sorted(s) == sorted(t) 