class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        #need a monotonic stack
            #where temps are only increasing
            #and top element is most likely to be resolved upon next iteration
        

        result = [0] * len(temperatures)

        stack = []

        for idx, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:

                result[stack[-1][1]] = idx - stack[-1][1]
                stack.pop()
            
            stack.append([temp, idx])
        
        return result

