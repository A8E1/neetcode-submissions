class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passedValues = {} # track which index we've passed through already using a dictionary
        # val (key) -> index (value)
        for i, j in enumerate(nums):
            # establish the diff for each interation, before checking the current index
            diff = target - j 
            if diff in passedValues:
                return [passedValues[diff], i]
            passedValues[j] = i
                

                

            