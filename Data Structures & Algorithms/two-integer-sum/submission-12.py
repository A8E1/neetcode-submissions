class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #a + b = c
        #each iteration, i have a and c, but not sure of a b
            #search a data structure for the b, if found, we return indices
            #if not found, we store the current a and it's index for a potential look up

        potentialA = {}

        for index, elem in enumerate(nums):
            num = target - elem
            if num in potentialA:
                return [potentialA[num], index]
            else:
                potentialA[elem] = index
        