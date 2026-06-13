class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack: # case 1: minStack is empty, so populate with val
            newMinVal = val
        elif val < self.minStack[-1]: # case 2: val is smaller so we need to replace minStack
            newMinVal = val
        else: #case 3 - value is larger or equal 
            newMinVal = self.minStack[-1] # keeps the value the same
        
        self.minStack.append(newMinVal) # always appends the newMinVal

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop() # why do we have to pop always 
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
