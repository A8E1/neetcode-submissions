class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0] * len(temperatures)

        for ind, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                gap = ind - stack[-1][1]
                res[stack[-1][-1]] = gap
                stack.pop()

            stack.append([temp, ind])
        
        return res
        