class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_v = nums[0]

        for num in nums:
            min_v = min(min_v, num)
        return min_v
        