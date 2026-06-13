class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force: sort array using .sort
        #have a counter that increments when "longest consecutive seq" conditions are met
        #have a max length that is replaced when counter exceeds it
        if nums == []:
            return 0
        
        nums.sort()
        print(nums)
        consecutive_count = 1
        max_count = 1
        for i in range(0, len(nums)-1):
            if nums[i] == (nums[i+1]-1):
                consecutive_count+=1
            elif nums[i] != nums[i+1]:
                consecutive_count = 1

            if consecutive_count > max_count:
                max_count = consecutive_count

        return max_count