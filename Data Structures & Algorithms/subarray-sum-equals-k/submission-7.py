class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixes = {0:1}
        curSum = 0
        counter = 0

        for num in nums:
            curSum += num

            diff = curSum - k

            counter += prefixes.get(diff, 0)

            prefixes[curSum] = prefixes.get(curSum, 0) + 1
        
        return counter
        