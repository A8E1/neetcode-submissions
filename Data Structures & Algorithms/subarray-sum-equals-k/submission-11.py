class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixDict = { 0:1 }
        curSum = 0
        res = 0


        #prefix calculation: curSum - prefix = k
        #prefix = curSum - k
        for num in nums:
            curSum += num
            
            diff = curSum - k

            res += prefixDict.get(diff, 0)

            prefixDict[curSum] = prefixDict.get(curSum, 0) + 1
        
        return res


