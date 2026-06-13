class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}

        for index, num in enumerate(nums):
            if target - num in num_index:
                return [num_index[target - num], index]
            num_index[num] = index