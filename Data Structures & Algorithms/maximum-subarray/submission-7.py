class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #array has to be contiguous aka all nums right next to each other
        #auto reset if sum is (-), highest arr will start with next num no matter what
        #(-) nums only make sum <


        currSum = 0
        maxSubArr = nums[0]

        for i in range(len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[i]
            maxSubArr = max(maxSubArr, currSum)
        
        return maxSubArr




