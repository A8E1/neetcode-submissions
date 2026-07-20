class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        #i think the strat here is to initialize a stack
        #iterate thru each val in temperatures
        #when the curr value is > than the top value of the stack
        #we pop it, and get that popped val's index use it to find the exact result
        #array index to populate, and then subtract curr_index - popped_index to find
        #num of days still a larger temp was detected
        #if no greater temp found, the result array remains untouched, and we return appropriately


        stack = []

        for ind, temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                popped_ind, popped_temp = stack.pop()

                num_of_days = ind - popped_ind

                res[popped_ind] = num_of_days

            stack.append([ind, temp])
        
        return res