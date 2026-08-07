class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_seq = 0
        
        for num in nums:
            if num-1 not in nums:
                cur_seq = 1
                seq = num+1
                while seq in nums:
                    cur_seq +=1
                    seq+=1
                max_seq = max(max_seq, cur_seq)
        
        return max_seq
                