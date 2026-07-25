class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #plan: apply binary search on the rows of the matrix to find target row

        #let's figure out how to do that
        #normal binary search algo goes like:
            #assign left at 0, right at end of list-1
            #using while l <= r
                #find mid point of array (l + r) // 2
                #see if element at mid point index is less than target
                    #assign l = mid + 1
                #see if element at mid point index is greater than target
                    #assign r = mid - 1
                #if element doesn't pass any of those conditions, we've found target
        
        #how do we manipulate that standard algorithm to apply to rows in this situation
        #translate each line
        #l would still be assigned 0, r would be assigned the m-1, since m is # of rows
            #m would be gotten by using len(matrix)
        #mid would still be calculated the same way (r + l) // 2
        #using while l <= r
            #if mid row's first index is greater than target
                #r = mid - 1
            #if mid row's last index is less than target
                #l = mid + 1
            
        
        l, r = 0, len(matrix)-1
        row_mid = 0
        while l <= r:
            row_mid = (l + r) // 2

            if matrix[row_mid][0] > target:
                r = row_mid - 1
            elif matrix[row_mid][-1] < target:
                l = row_mid + 1
            else:
                break
        
        l, r = 0, len(matrix[row_mid])-1
        
        while l <= r:
            mid = (l + r) // 2

            if matrix[row_mid][mid] > target:
                r = mid - 1
            elif matrix[row_mid][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False
