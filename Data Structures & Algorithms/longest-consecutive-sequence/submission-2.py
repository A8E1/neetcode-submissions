class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums = set(nums)
        longestConsecutive = 0
        for num in nums:
            if num-1 in setOfNums:
                continue
            consecutive = 0
            while num in setOfNums:
                consecutive += 1
                num+=1
            longestConsecutive = max(longestConsecutive, consecutive)

        return longestConsecutive