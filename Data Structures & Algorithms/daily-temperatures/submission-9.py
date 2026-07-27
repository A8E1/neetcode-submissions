class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #the stack signal that glares at me after reading this question is the wording here:
            #"where result[i] is the number of days after the ith day 
            #before a warmer temperature appears on a future day"
        #this is a translated way of saying: future/more recent unresolved values, (can) resolve past ones
        #this is a stack signal! 
        #particularly, by the nature of this question, we'd use a monotonic decreasing stack
        #the decreasing direction is because we pop when a hotter temp comes along and can
        #give us the # of days after the ith day that a warmer temp comes by
        #the fact that a HOTTER temp is what resolves past elements, means we store decreasingly colder temps
        #the decreasing nature of the stack's values also mirrors their priority level of being popped, 
        #since there could be a scenario where 
        #slightly hotter days can only pop a given portion of stack elements, and that portion needs to be
        #at the top of the stack

        #time: O(n), space O(n)


        stack = []

        res = [0] * len(temperatures)

        for ind, temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                popped_ind, _ = stack.pop()
                res[popped_ind] = ind - popped_ind
            
            stack.append([ind, temp])
        
        return res
        