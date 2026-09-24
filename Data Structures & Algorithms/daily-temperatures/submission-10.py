class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Days without a future warmer temp keep 

        res = [0] * len(temperatures)

        stack = []


        for idx, temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                popped_day = stack.pop()

                res[popped_day[0]] = idx - popped_day[0]
        
            stack.append([idx, temp])
        
        return res