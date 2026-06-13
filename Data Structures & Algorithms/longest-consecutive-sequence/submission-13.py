class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        nums = set(nums)
        
        #no more dupe values in nums list

        curr_seq = 1
        max_seq = 0

        for num in nums:
            if num - 1 not in nums:
                while num+curr_seq in nums:
                    curr_seq+=1
                max_seq = max(curr_seq, max_seq)
                curr_seq = 1
        
        return max_seq
            

        