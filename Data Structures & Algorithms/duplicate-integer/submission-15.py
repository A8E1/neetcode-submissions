class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False




       
    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        # make a hashset
        seen = set()

        # loop through nums to either populate hashset or return False if value is seen
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
       '''