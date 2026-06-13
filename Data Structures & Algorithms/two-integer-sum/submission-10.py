# the idea is that for sums its a + b = c

# we are trying to find a and b, but we have c

# and for each iteration we have a potential a 

# so for each iteration we have an a and c

# to find that b, we can just use basic math principles, bc if a + b = c, then c - a = b

# and if that is the case, both a and b exist within the nums list, we have our two integers

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #the As and Bs that lead to our target C
        sums = {}


        #iterate thru each elem of list
        for index, a in enumerate(nums): 
            #find corresponding num that = target
            b = target - a

            #find b in sums list
            if b in sums:
                return [sums[b], index]
            sums[a] = index              
            
        

