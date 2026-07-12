class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #use a stack to take in all inputs
        #when reaching an operand, pop previous elements until stack is empty
        #use a result variable that you combine operands + operations with


        stack = []

        operator_set = set(["+", "-", "*", "/"])
        for c in tokens:
            if c not in operator_set:
                stack.append(int(c))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if c == "+":
                    stack.append(op1 + op2)
                elif c == "-":
                    stack.append(op1 - op2)
                elif c == "*":
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 / op2))

        return stack[-1]