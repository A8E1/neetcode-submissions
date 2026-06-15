class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0

        prefixSums = { 0:1 }

        curSum = 0
        for num in nums:
            curSum += num

            diff = curSum - k

            count += prefixSums.get(diff, 0)

            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        
        return count 

        