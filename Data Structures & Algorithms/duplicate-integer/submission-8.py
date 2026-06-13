class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #solution example that is O(n log n), but has an O(1) space complexity
        nums.sort()

        for i in range(len(nums)-1):
            #comparison sorts are always O(n log n)
            if nums[i] == nums[i+1]:
                return True

        return False