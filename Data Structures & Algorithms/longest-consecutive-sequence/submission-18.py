class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        #dupes gone

        max_len = 0

        for num in nums_set:
            if num-1 not in nums_set:
                sequence_len = 1
                while num+1 in nums_set:
                    sequence_len += 1
                    num += 1


                max_len = max(max_len, sequence_len)
        return max_len
            