class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # will only ever be populated with opening stack
        validParenthesis = {'}': '{', ']': '[', ')': '('}

        for char in s:
            if char in validParenthesis: # executes when closing parenthesis is detected
                if stack and stack[-1] == validParenthesis[char]: # checks if empty and if top of stack matches 
                    stack.pop()
                else: 
                    return False # returns false because top of stack deosn't match with key
            else: 
                stack.append(char) # append opening bracket

        return True if not stack else False


