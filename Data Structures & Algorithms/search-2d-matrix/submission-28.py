class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #why u used it
        #how techs work with each other
        
        #objective: return true if target exists, false otherwise

            #every row is in ascending order
            #rows themselves in ascending order

        #algo: binary search

        #initial binary search on rows to find the most likely row that target exists
            #search space: rows in matrix
                #if matrix[m][0] > target:
                    #r = m-1
                #if matrix[m][-1] < target:
                    #l = m+1
        
        plausible_row = []
        l, r = 0, len(matrix)-1
        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                plausible_row = matrix[m]
                break
        

        l, r = 0, len(plausible_row)-1
        while l <= r:
            m = (l + r) // 2

            if plausible_row[m] == target:
                return True
            
            if plausible_row[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False
            


        







