class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #subarray has to be contiguous aka the 
        #numbers have to be right next to each other

        #if the sum of the subarray is < the next number, we can start at that number
        
        maxSubArr = nums[0]
        currSum = 0

        for i in range(len(nums)):
            if currSum < 0:
                currSum = 0
                #starting at the next number
                #since if it is negative it auto means pos numbers r the maxSubArr
                #and if the next num is neg if currSum still (-) it'll decrease the num even more
                #so it means next num is auto the greatest subArr

            currSum += nums[i]
            maxSubArr = max(maxSubArr, currSum)

        return maxSubArr




