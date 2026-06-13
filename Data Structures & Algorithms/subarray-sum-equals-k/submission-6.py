class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixFrequency = { 0:1 }

        curSum = 0
        res = 0

        for num in nums:
            curSum+=num

            diff = curSum - k
            #curSum - diff = k

            res += prefixFrequency.get(diff, 0)

            prefixFrequency[curSum] = prefixFrequency.get(curSum, 0) + 1
        
        return res

        #2*, -1, 1, 2 | k = 2
        #curSum = 2
        #diff = 0
        #res = 1
        #prefixFreq[curSum] = 1

        #2, -1*, 1, 2 | k = 2
        #curSum = 1
        #diff = -1
        #res = 1
        #prefixFreq[curSum] = 1

        #2, -1, 1*, 2 | k = 2
        #curSum = 2
        #diff = 0
        #res = 2
        #prefixFreq[curSum] = 2

        #2, -1, 1, 2* | k = 2
        #curSum = 4
        #diff = 2
        #res = 4
        #prefixFreq[curSum] = 1





