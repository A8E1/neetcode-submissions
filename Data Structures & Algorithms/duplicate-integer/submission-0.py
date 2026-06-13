class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use hash sets
        numsAppeared = set()

        for i in nums:
            if i in numsAppeared:
                return True
            numsAppeared.add(i)
        return False
        