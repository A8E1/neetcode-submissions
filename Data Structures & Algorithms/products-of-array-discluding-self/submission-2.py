class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for index, num in enumerate(nums):
            product = 1

            for i in range(len(nums)):

                if num != nums[i] or index != i:
                    product *= nums[i]
            output.append(product)
        
        return output