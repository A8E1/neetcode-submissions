# the idea is that for any addition its a + b = c

# we are trying to find the INDEX of a and b, but we have c

# and for each iteration we have a potential a 

# so for each iteration we have an a and c

# to find that b, we can just use basic math principles, bc if a + b = c, then c - a = b

# and if that is the case, and both a and b exist within the nums list, we have our two indicies

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #the hashmap to store potential 'B's for each 'A' of the nums list
        sums = {}


        #iterate thru each elem of list, each elem = a potential 'A' value
        for index, a in enumerate(nums): 
            #find corresponding 'B' value that A + B = target
            b = target - a

            #find 'B' in hashmap
            if b in sums:
                #return past 'A' and 'B' index values
                return [sums[b], index]
            #if the 'B' value for the iteration is NOT in the hashmap, we store the current 'A' value and it's index

            #that way, if we find another element that has a 'B' value of a past 'A' we can pull that from the hashmap
            sums[a] = index              
            
        

