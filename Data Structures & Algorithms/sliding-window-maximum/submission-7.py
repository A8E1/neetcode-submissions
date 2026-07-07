class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        l = 0

        res = []

        for r in range(len(nums)):
            #while the queue exists and has numbers in it
            #and, if the new number processed is bigger than 
            #numbers prior to it,
            #we will eliminate all those numbers, since with the addition of this new number
            #those numbers that are older indices won't ever be accessed
            while q and nums[r] > nums[q[-1]]:
                #remove numbers at the front (oldest)
                q.pop()

            q.append(r)

            #if the left bound index is > the oldest index in the queue
            #pop that old index, means window shifted
            if l > q[0]:
                q.popleft()
            

            #once window length == given k, 
            #append greatest element, and shift window
            #we use the queue to track the greatest element
            #front of the queue will hold the largest element in the window
            #this is because we remove all older indices that would be at the front
            #that are smaller, and we remove all older indices that exist outside of the 
            #window
            #this keeps the largest + relevant indices at the front of the queue
            if (r - l + 1) == k:
                res.append(nums[q[0]])
                l+=1
        
        return res
            




        