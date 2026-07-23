class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #the plan: first apply binary search to find the correct row

        #then apply binary search to find the specific target in that row


        #what defines the correct row:
            #if the target exists btwn two rows
            #if its greater than row 1's first index, and less than row 2's first index
            #we then know the target exists in row 1
        #possibilities when processing:
            #row1[0] > target < row2[0] (row found)
            #row1[0], row2[0] < target 
            #target > row1[0], row2[0]

        
        #then we apply binary search on that merged row


        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS-1

        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid+1
            elif target < matrix[row][mid]:
                r = mid-1
            else:
                return True
        
        return False



