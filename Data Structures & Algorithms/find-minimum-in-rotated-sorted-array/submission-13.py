class Solution:
    def findMin(self, nums: List[int]) -> int:

        #rotated array: consists of two halves
            #1st half (from the left, 0->) represents rotated half
            #2nd half (from the right, <-nums[-1]) represents non-rotated half

        #edge case: array rotated len(array) times becomes normal ascending sorted arr

        #with the general case:
            #the min is == pivot point btwn the two halves
        
        #edge case:
            #min is == beginning of the array/technical pivot which is at idx 0

        
        #approach is going to be centered on trying to locate that pivot


        l, r = 0, len(nums)-1

        #search space: elements from 0 -> last idx of array
        
        #monotonic condition/elimination condition:
            #if m is in the left half/rotated half, min is not there
                #if nums[m] > nums[l] and nums[m] < nums[r]:
                    #min = min(min, nums[m])
                    #l = m + 1
            #if m is in the right half/non-rotated half, min is a possibility
                #if nums[r] > nums[m] and nums[l] > nums[l]
                    #min = min(min, nums[m])
                    #r = m
        min_val = float('infinity')
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        return nums[r]
            



