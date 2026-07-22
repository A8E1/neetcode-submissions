class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #iterate using first


        outer_l, outer_r = 0, len(matrix)-1

        while outer_l <= outer_r:

            array_selection = (outer_l + outer_r) // 2
            if matrix[array_selection][0] < target:
                outer_l = array_selection + 1
            elif matrix[array_selection][0] > target:
                outer_r = array_selection - 1
            else:
                return True
        #when outer_l == outer_r there r two possibilities:
            #target in the agreed array
            #target is not in the agreed array
            #now, we run normal binary search on the selected array
        target_row = outer_r
        if target_row < 0: return False
        
        inner_l, inner_r = 0, len(matrix[target_row])-1
        while inner_l <= inner_r:
            mid = (inner_l + inner_r) // 2

            if matrix[target_row][mid] < target:
                inner_l = mid + 1
            elif matrix[target_row][mid] > target:
                inner_r = mid - 1
            else:
                return True
        
        return False
