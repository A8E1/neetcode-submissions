class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        #create def. values of the output arr
        prefix = 1
        #def. value for prefix of index 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
            #important for the multiplication to happen AFTER since the prefix relates to the value prior
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
            #important for the multiplication to happen AFTER since the postfix relates to the value prior
        return output