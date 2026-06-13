class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potentialAddends = {}
        #key: addend, value: index

        for i, elem in enumerate(nums):
            addend2 = target - elem

            if addend2 in potentialAddends:
                return [potentialAddends[addend2], i]
            else:
                potentialAddends[elem] = i
        
