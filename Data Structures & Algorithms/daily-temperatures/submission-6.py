class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0] * len(temperatures)

        for ind, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                stackInd = stack[-1][1]
                gap = ind - stackInd
                res[stackInd] = gap
                stack.pop()
            
            stack.append([temp, ind])
        
        return res
        