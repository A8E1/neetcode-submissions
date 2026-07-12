class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        op_set = set(["+", "-", "/", "*"])
        for c in tokens:
            if c not in op_set:
                stack.append(int(c))
            else:
                op1 = stack[-1]
                stack.pop()
                op2 = stack[-1]
                stack.pop()

                if c == "+":
                    res = op1 + op2
                    stack.append(res)
                elif c == "-":
                    res = op2 - op1
                    stack.append(res)
                elif c == "*":
                    res = op1 * op2
                    stack.append(res)
                else:
                    res = op2 / op1
                    res = int(res)
                    stack.append(res)
        
        return stack[-1]
        