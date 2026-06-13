class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums = set(nums)
        lengthOfConsecutive = 0

        for i in range(len(nums)):
            currNum = nums[i]
            if currNum-1 not in setOfNums:
                length = 1
                while currNum+1 in setOfNums:
                    length+=1
                    currNum+=1
                if length > lengthOfConsecutive:
                    lengthOfConsecutive = length
        return lengthOfConsecutive
                