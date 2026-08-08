class Solution:
    def isValid(self, s: str) -> bool:
        c_t_o = {"}" : "{", "]" : "[", ")" : "("}

        stack = []

        for c in s:
            if c in c_t_o:
                if stack and stack[-1] == c_t_o[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False