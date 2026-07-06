class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #seems pretty straight-forward, not understanding why this is a hard
        #we have a left variable instantiated at 0, and a right loop variable iterating thru the list
        #we have an if condition within the loop enforcing the window being of k size, and if it isn't, we move l upwards.
        #if passing that condition, we check if we have a new max
        #the question is, what state can we implement to make sure to we track the greatest element in the window in an efficient way
        #the one thing i'm thinking about is having a "max_int" variable that is replaced with a max() operation for every new int added
        #but the caveat with that is that we need to make sure the max_int we assign exists in the window we're looking at
        #cuz theoretically, max_int could decrease
        #the way I'm thinking is using some sort of O(1) look-up data structure to locate the existance of a num
        #i think for sure a hashmap would help here. but the question is where does it fit? we store each value, kick out the left
        #bound's value if it doesn't exist anymore in the window. and the reason we choose hashmap over set is because the window
        #could hold dupe values, and we need to add those values in, since the removal of an old dupe doesn't mean that value
        #doesn't exist in the window anymore. so I'm thinking of the values representing frequencies we decrement, and we remove
        #the pair if the key == 0. this should be a good enough state. let's code
        
        res = []

        l = 0

        max_win_val = nums[0]

        win_count = {}

        for r in range(len(nums)):
            #build window hash map so we can look-up if max is truly replaced
            win_count[nums[r]] = win_count.get(nums[r], 0) + 1

            max_win_val = max(max_win_val, nums[r])

            if (r-l+1) > k:
                win_count[nums[l]] -= 1

                if win_count[nums[l]] == 0:
                    win_count.pop(nums[l])

                l+=1
            
            if max_win_val not in win_count:
                max_win_val = nums[r]
                for num in win_count.keys():
                    max_win_val = max(max_win_val, num)
            if (r-l+1) == k:
                res.append(max_win_val)
        
        return res
            




        
