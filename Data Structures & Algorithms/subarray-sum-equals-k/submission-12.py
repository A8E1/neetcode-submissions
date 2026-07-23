class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumsDict = { 0: 1}
        res = 0
        curSum = 0

        for num in nums:

            curSum += num

            diff = curSum - k

            res += prefixSumsDict.get(diff, 0)

            prefixSumsDict[curSum] = prefixSumsDict.get(curSum, 0) + 1

        
        return res

