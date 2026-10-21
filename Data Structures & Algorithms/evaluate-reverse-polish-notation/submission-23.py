class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        op_set = set(["+", "-", "*", "/"])
        stack = []
        for i in range(len(tokens)):

            if tokens[i] in op_set:
                right_op = stack[-1]
                stack.pop()
                left_op = stack[-1]
                stack.pop()
                res = 0
                if tokens[i] == "+":
                    res = left_op + right_op
                elif tokens[i] == "-":
                    res = left_op - right_op
                elif tokens[i] == "*":
                    res = left_op * right_op
                else:
                    res = int(left_op / right_op)

                stack.append(res)
            else:
                val = int(tokens[i])
                stack.append(val)
        
        return stack[-1]



