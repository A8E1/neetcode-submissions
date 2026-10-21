class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        #plan: first locate matrix row, then locate specific index

        #elimination criteria: 
            #r = m - 1
                #if row_at_m[0] > target
            #l = m + 1
                #if row_at_m[-1] < target

        plausible_row = []

        l, r = 0, len(matrix)-1
        while l <= r:
            
            m = (l + r) // 2
            cur_row = matrix[m]

            if target > cur_row[-1]:
                l = m+1
            elif target < cur_row[0]:
                r = m-1
            else:
                plausible_row = cur_row
                break
        if plausible_row == []:
            return False
        l, r = 0, len(plausible_row)-1
        while l <= r:
            m = (l + r) // 2
            if target > plausible_row[m]:
                l = m + 1
            elif target < plausible_row[m]:
                r = m - 1
            else:
                return True
        
        return False
        