class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #nums is in ascending order

        #brute force:
            #output arr instantiated with [0] * len(nums)
            #iterate across nums and put num[i]*num[i] in output[i]
            #.sort() output to get it in ascending order

        #the fact that the input arr is in ascending order
        #tells me that two pointers is a possibility
        #I wonder if we could do something like
            #calculate output with one for loop pass
            #sort using two pointers

        
        squares = [1] * len(nums)

        for i in range(len(nums)):
            squares[i] = nums[i]*nums[i]
        
        l, r = 0, len(squares)-1

        output = [1] * len(squares)
        currOutputInd = len(squares)-1
        while l <= r:

            if squares[r] >= squares[l]:
                output[currOutputInd] = squares[r]
                currOutputInd-=1
                r-=1
            else:
                output[currOutputInd] = squares[l]
                currOutputInd-=1
                l+=1
            
        return output

            



