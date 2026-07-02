class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumFreq = {0:1}
        curSum = 0
        #k = curSum - diff
        res = 0
        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSumFreq.get(diff, 0)

            prefixSumFreq[curSum] = prefixSumFreq.get(curSum, 0) + 1
        
        return res
        
    