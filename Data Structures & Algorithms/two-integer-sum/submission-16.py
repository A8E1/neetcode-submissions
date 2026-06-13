class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # element : index
        prevMap = {}

        for index, element in enumerate(nums):
            # target = a + b, we know target,
            difference = target - element 

            if difference in prevMap:
                return [prevMap[difference], index]
            
            prevMap[element] = index



            