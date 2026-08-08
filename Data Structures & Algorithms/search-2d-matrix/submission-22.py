class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        chosen_row = -1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                chosen_row = mid
                break
        

        l, r = 0, len(matrix[chosen_row])-1

        while l <= r:
            mid = (l + r) // 2

            if matrix[chosen_row][mid] < target:
                l = mid + 1
            elif matrix[chosen_row][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False