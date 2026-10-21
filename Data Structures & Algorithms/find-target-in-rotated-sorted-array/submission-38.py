class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #O(log n) => binary search algorithm
        #other important signals: 
            #array was originally in sorted ascending order
                #potentially ordered search space we can evaluate
            #objective: locate a specific target value (if it exists)

        #1) objective
            #find a specific target value
        #2) search space
            #the indices of the input array
        #3) exploit
            #certain portions of the rotated array are still sorted in ascending order. 
            #we will exploit that using numerical comparison
        #4) invariant
            #if the target exists, it's preserved in the interval: [l, r]
            #inclusive, since we are locating a specific value
            #not a boundary value for example where valid candidates can't
            #be safely eliminated 
        #5) elim proof
            #calculate midpoint
            #use it to identify the sorted portions of the array
            #then using a range test to identify if the target lives there
            #based on that, we can safely eliminate that sorted portion
        #6) what will my implementation terminate
            #we will be terminating regions of the input array
            #that do not have the target value if it exists, living there.
            #we do that safely, leveraging the structure of the rotated array

        

        l, r = 0, len(nums)-1
        while l<=r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            #now elimination proof: identify sorted portion first.

            #is [l, m] a sorted sub-array?
            if nums[m] >= nums[l]:
                #if so, range test to see if target lives here

                if nums[m] > target and target >= nums[l]:
                    r = m-1
                else:
                    l = m+1
            else:

                if nums[r] >= target and target > nums[m]:
                    l = m+1
                else:
                    r = m-1
            
        
        return -1









