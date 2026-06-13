class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for index, integer in enumerate(nums):
            # target - integer = diff
            diff = target - integer

            if diff in prev:
                return [prev[diff], index]
                
            prev[integer] = index
            



            