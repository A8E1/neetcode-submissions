class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #output: 
            #result list holding list of unique combinations of 3 numbers
            #found in input list that equal 0
        #object being searched:
            #an input array of numbers that could contain duplicates in
            #any order
        #invariant/condition:
            #only add combinations that do not
            #contain the same numbers as a already
            #added winning combination
        #brute force:
            #check every combination of three numbers that can
            #possibly exist in the array and add only ones that haven't
            #added to the list
        #repeated work:
            #with an unsorted list, we are indiscriminately comparing
            #values. therefore we might be comparing values that
            #had no possibility ever equalling 0. 
            #taking a 3, and for the second loop taking a 7
        #state that can move it:
            #sorting the list, so movement throughout the list
            #has an effect on the output
            #an outer loop that iterates through each index of the list
            #an inner loop that tracks two pointers where the movement of 
            #the ptrs depends on the three_sum being >/< 0.
            #once a winning combination is detected, we add to the result
            #list, and then we iterate both pointers, with a cautionary 
            #while loop to make sure they don't 
            #equal their previous pointer values to avoid dupes. 
        #redesign algo:


        nums.sort()
        result_list = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum == 0:

                    result_list.append([nums[i], nums[l], nums[r]])

                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif three_sum > 0:
                    r-=1
                else:
                    l+=1

        return result_list