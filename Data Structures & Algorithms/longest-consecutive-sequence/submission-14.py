class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sequences = numbers that are +1 greater than the last
        #START = numbers that don't have any numbers exactly -1 anywhere in the arr

        #duplicates can exist, but have no effect on our output, so let's get rid of them

        num_set = set(nums)

        sequence_tracker = 0
        for num in num_set:
            if num-1 not in num_set:
                #now we've isolated a potential sequence start
                length = 1
                while num+length in num_set:
                    length+=1
                    #stops when sequence ends
                sequence_tracker = max(sequence_tracker, length)
        
        return sequence_tracker
