class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #U: Understand
            #Constraint -> Complexity Inference (length of nums array is bounded by ~10^4 therefore n time complexity solution is within our budget )
            #2-3 Edge cases
                #empty list
                #list with one value
            
            #1 handwritten example
                # nums = [2,-1,1,2], k = 2

        #M: Match
            #this is simply a for loop iteration question with the added 
            #understanding of prefix sums, since we need to find all contiguous subarrays that equal k
            #the reason why sliding window is not something we can consider, is because the window state can't evolve
            #contiguous subarrays whose sum equal k can exist outside of a current window size
        #P: Plan
            #State
                # a diff variable calculated for each iteration
                # a dictionary tracking each current sum as the loop iterates and it's frequency, since the cursum can decrement

            #Invariant
                # 
            #Increment step 
            #Answer
            #Resolve
        #I: Implement
        #R: Review
        #E: Evaluate


        prefixSums = { 0:1 }

        curSum = 0

        res = 0

        for num in nums:
            #this will be our running sum across the entire array
            curSum += num

            #diff is the difference between the target value and our current running sum
            #diff represents a potential sub array that exists within our array
            #the way we check if the diff sub array is found in our array is by using that 
            #dictionary that we keep track of sums and their frequencies

            diff = curSum - k

            res += prefixSums.get(diff, 0)

            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
    
        return res


            


