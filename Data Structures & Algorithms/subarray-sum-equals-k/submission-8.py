class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = { 0:1 }
        #for the case of a initial subarray sum == k and diff = 0

        curSum, res = 0, 0
        for num in nums:
            curSum += num

            diff = curSum - k
            #curSum - diff = k
            
            res += prefixSums.get(diff, 0)

            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        
        return res
