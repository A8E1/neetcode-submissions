class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potentialAddends = {}

        for index, num in enumerate(nums):
            num2 = target - num
            if num2 in potentialAddends:
                return [potentialAddends[num2], index]
            else:
                potentialAddends[num] = index
        
        return None
        
