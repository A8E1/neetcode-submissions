class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        op_set = set(["*", "-", "/", "+"])

        for c in tokens:

            if c not in op_set:
                stack.append(int(c))
            
            else:
                if c == "+":
                    op2 = stack.pop()
                    op1 = stack.pop()

                    res = op1 + op2
                    stack.append(res)
                elif c == "-":
                    op2 = stack.pop()
                    op1 = stack.pop()

                    res = op1 - op2
                    stack.append(res)
                elif c == "/":
                    op2 = stack.pop()
                    op1 = stack.pop()

                    res = op1 / op2
                    stack.append(int(res))
                elif c == "*":
                    op2 = stack.pop()
                    op1 = stack.pop()

                    res = op1 * op2
                    stack.append(res)

        
        return stack[-1]