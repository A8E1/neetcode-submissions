class Solution:
    def isValid(self, s: str) -> bool:
        parenKey = { ")":"(", "]":"[", "}":"{"}

        stack = []

        for i in range(len(s)):

            if s[i] in parenKey:
                if stack and stack[-1] == parenKey[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        if stack:
            return False
        return True
            