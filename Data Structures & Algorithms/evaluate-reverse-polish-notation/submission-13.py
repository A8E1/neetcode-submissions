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
                prev_res = stack[-1]
                stack.pop()

                if c == "+":
                    res = op1 + prev_res
                    stack.append(res)
                elif c == "-":
                    res = prev_res - op1
                    stack.append(res)
                elif c == "*":
                    res = op1 * prev_res
                    stack.append(res)
                else:
                    res = prev_res / op1
                    res = int(res)
                    stack.append(res)
        
        return stack[-1]
        